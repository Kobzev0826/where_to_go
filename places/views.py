from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db import connection

from places.models import Place


def show_start_page(request):
    places = []
    for place in Place.objects.all():
        places.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lon, place.lat],
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse("place-detail", args=[place.id]),
                },
            },
        )
    context = {
        "title": "Куда пойти",
        "places": {"type": "FeatureCollection", "features": places},
    }
    return HttpResponse(render(request, "index.html", context))


def show_place(request, place_id):

    requested_place = Place.objects.prefetch_related("images").filter(id=place_id).first()

    if not requested_place:
        return JsonResponse({"error": "Place not found"}, status=404)

    images = [image.image.url for image in requested_place.images.all()]

    place = {
        "title": requested_place.title,
        "imgs": images,
        "description_short": requested_place.short_description,
        "description_long": requested_place.detail_description,
        "coordinates": {
            "lat": requested_place.lat,
            "lng": requested_place.lon,
        },
    }
    return JsonResponse(place)
