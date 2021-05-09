from django.http.response import HttpResponse
from properties.forms import PropertyAmenitiesForm, PropertyTypeForm
from django.shortcuts import render
from django.http import JsonResponse

from . models import PropertType, Properties, PropertyAmenities
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
        form = PropertyTypeForm(request.POST, None)
        if form.is_valid():
            print("This is the response data ---------------------><><> form is valid")
            name = request.POST.get('name')
            notes = request.POST.get('notes')
            
            response_data['name'] = name
            response_data['notes'] = notes

            create_obj = PropertType.objects.create(
                name = name,
                notes = notes
                )
            response_data['name'] = create_obj.name
            response_data['notes'] = create_obj.notes
            response_data['created_date'] = create_obj.created_date
            response_data['updated_date'] = create_obj.updated_date
            
            return JsonResponse(response_data)
        else:
            return JsonResponse({"error": form.errors}, status=400,safe=False)
    return render(request,"properties/property-type.html",  {'property_types':property_types})  

def property_ammenities(request):
    form = PropertyAmenitiesForm()
    response_data = {}
    property_amenities = PropertyAmenities.objects.all()
    context = {
        "form":form,
        "property_amenities":property_amenities
    }

    if request.method == 'POST':
        form = PropertyTypeForm(request.POST, None)
        if form.is_valid():
            print("This is the response data ---------------------><><> form is valid")
            name = request.POST.get('name')
            notes = request.POST.get('notes')

            create_obj = PropertyAmenities.objects.create(
                name = name,
                notes = notes
                )
            response_data['name'] = create_obj.name
            response_data['notes'] = create_obj.notes
            response_data['created_date'] = create_obj.created_date
            response_data['updated_date'] = create_obj.updated_date 
            return JsonResponse(response_data)
        else:
            return JsonResponse({"error": form.errors}, status=400,safe=False)
    return render(request,"properties/property-ammenities.html", context)     
