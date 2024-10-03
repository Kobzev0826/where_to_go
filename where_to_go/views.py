from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from places.models import Place
from django.http import HttpResponseNotFound, JsonResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def show_start_page(request):
    template = loader.get_template('index.html')
    places = []
    for place in Place.objects.all():
        places.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"place/{place.id}"
            }
        })
    context = {'title':'Куда пойти',  'places': {"type": "FeatureCollection","features": places}}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def show_place(request, place_id):
    requested_place = get_object_or_404(Place, id=place_id)
    images = [image.image.url for image in requested_place.images.all()]


    place = {
        'title': requested_place.title,
        'imgs': images,
        "description_short": requested_place.short_description,
        "description_long": requested_place.detail_description,
        'coordinates': {
            "lat": requested_place.lat,
            "lng": requested_place.lon
        }
    }
    return JsonResponse(place)