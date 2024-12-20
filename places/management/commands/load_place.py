import requests
from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError, transaction
from loguru import logger
from requests.exceptions import RequestException, ConnectionError, Timeout
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from places.models import Image, Place


class Command(BaseCommand):
    help = "Add new place from json url"

    def add_arguments(self, parser):
        parser.add_argument("json_url", type=str, help="Json url")

    @retry(
        stop=stop_after_attempt(5),  # Максимум 5 попыток
        wait=wait_exponential(
            multiplier=2,
            min=2,
            max=10,
        ),
        retry=retry_if_exception_type(
            (ConnectionError, Timeout),
        ),
    )
    def get_http(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

        except RequestException as e:
            logger.error(f"HTTP error occurred: {e}")
            return None

        return response

    def handle(self, *args, **kwargs):
        json_url = kwargs["json_url"]
        response = self.get_http(json_url)
        if not response:
            return
        try:
            place_raw = response.json()
        except ValueError as e:
            logger.error(f"JSON decoding error: {e}")
            return

        try:
            with transaction.atomic():
                try:
                    place, created = Place.objects.get_or_create(
                        title=place_raw["title"],
                        defaults={
                            "short_description": place_raw["description_short"],
                            "detail_description": place_raw["description_long"],
                            "lat": place_raw["coordinates"]["lat"],
                            "lon": place_raw["coordinates"]["lng"],
                        },
                    )
                except MultipleObjectsReturned:
                    logger.error(
                        "Error: Multiple places found with the same title and lat,lng.",
                    )
                    return
                except IntegrityError:
                    logger.error("Database integrity error during place creation.")
                    return
                except KeyError as e:
                    logger.error(f"Missing key in JSON data: {e}")
                    return

                for index, image_url in enumerate(place_raw.get("imgs", [])):
                    image_response = self.get_http(image_url)
                    if not image_response:
                        logger.error(f"Failed to retrieve image at URL: {image_url}")
                        continue

                    try:
                        Image.objects.create(
                            place=place,
                            image = ContentFile(image_response.content, name=f"{place.pk}-{index}.jpg")
                        )
                    except IntegrityError:
                        logger.error("Database integrity error during image creation.")
                    except RequestException as e:
                        logger.error(f"HTTP error occurred while fetching image: {e}")
            logger.info(f"Successfully loaded new place {json_url}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
