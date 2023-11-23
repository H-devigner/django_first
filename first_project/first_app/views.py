from django.http import HttpResponse
from django.template import loader
from .models import Person

# Create your views here.

def first_app(request): #first view
    template = loader.get_template('firstHtml.html') #this view is related to this template
    person_data = Person.objects.all().values()
    context = {
        'person_data' : person_data
    }
    return HttpResponse(template.render(context, request))

def second_view(request):# but this view is rendering html directly 
    content_page = "Hello world from another view! <span style='color: red;'>yes</span>" 
    return HttpResponse(content_page)

def details(request, id):
    template = loader.get_template('details.html') # the details view
    person_item = Person.objects.get(id=id)
    context = {
        'person_item': person_item
    }
    return HttpResponse(template.render(context, request))

def main_page(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render()) # the main view /