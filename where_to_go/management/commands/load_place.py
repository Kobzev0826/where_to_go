from django.core.files.base import ContentFile
import requests
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Add new place from json url'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='Json url')

    def get_http(self,url):
        response = requests.get(url)
        response.raise_for_status()
        return response

    def handle(self, *args, **kwargs):
        json_url = kwargs['json_url']
        response = self.get_http(json_url)
        place_raw = response.json()
        place, created = Place.objects.get_or_create(
            title=place_raw['title'],

            defaults={
                "short_description": place_raw['description_short'],
                "detail_description": place_raw['description_long'],
                "lat": place_raw['coordinates']['lat'],
                "lon": place_raw['coordinates']['lng'], },
        )

        for index, image_url in enumerate(place_raw['imgs']):
            image_obj = Image.objects.create(
                place=place,
            )
            image_response = self.get_http(image_url)
            image_content = ContentFile(image_response.content)

            image_obj.image.save(
                f'{place.pk}-{index}.jpg', image_content, save=True)