from django.http import HttpResponse
from django.template import loader
from places.models import Place

def show_start_page(request):
    template = loader.get_template('index.html')
    context = {'h4': 'Выберите место на карте2', 'title':'Куда пойти', 'places': Place.objects.all()}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)