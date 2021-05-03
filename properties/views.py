from django.shortcuts import render
from . models import PropertType, Properties
# Create your views here.

def index(request):
    properties = Properties.objects.all()
    context  = {
        'properties':properties
    }
    return render(request,"properties/index.html", context)

def property_types(request):
    property_types = PropertType.objects.all()
    context = {
       "property_types": property_types 
    }
    return render(request,"properties/property-type.html", context)