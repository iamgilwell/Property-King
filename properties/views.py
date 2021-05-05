from properties.forms import PropertyTypeForm
from django.shortcuts import render
from django.http import JsonResponse

from . models import PropertType, Properties
# Create your views here.

def index(request):
    properties = Properties.objects.all()
    context  = {
        'properties':properties
    }
    return render(request,"properties/index.html", context)

def property_types(request):
    form = PropertyTypeForm()
    property_types = PropertType.objects.all()
    context = {
        "form":form,
       "property_types": property_types 
    }
    return render(request,"properties/property-type.html", context)

def save_property_type(request):
    property_types = PropertType.objects.all()
    response_data = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        notes = request.POST.get('notes')

        response_data['name'] = name
        response_data['notes'] = notes
        print("This is the response data ---------------------><><>", response_data)

        create_obj = PropertType.objects.create(
            name = name,
            notes = notes,
            )
        

        print("This is the response data ---------------------><><> create_obj.latest", create_obj.objects)

        return JsonResponse(response_data)
    return render(request,"properties/property-type.html",  {'property_types':property_types})        
