from django.http import HttpResponse
from django.template import loader
from places.models import Place

def show_start_page(request):
    template = loader.get_template('index.html')
    places =  Place.objects.all()

    context = {'title':'Куда пойти', 'places': places}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)