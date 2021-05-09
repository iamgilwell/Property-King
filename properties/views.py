from django.http.response import HttpResponse
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
    # print("This is the response data ---------------------><><> save_property_type", request)
    if request.method == 'POST':
        print("This is the response data ---------------------><><> save_property_type", request)
        form = PropertyTypeForm(request.POST, None)
        # print("This is the response data ---------------------><><> form", form)
        if form.is_valid():
            property_type_obj = form.save(commit=False)
            print("This is the response data ---------------------><><> form is valid")
            name = request.POST.get('name')
            notes = request.POST.get('notes')
            
            # property_type_obj.save()
            response_data['name'] = name
            response_data['notes'] = notes
            # print("This is the response data ---------------------><><> name", name)

            # obj, created = PropertType.objects.get_or_create(
            #         name=name)
            # obj, created = PropertType.objects.get_or_create(
            #         name=name)
            # print("This is the response data ---------------------><><> obj", obj)
            # if created:
            #     print('its a new one, hooray!')
            # else:
            #     print('views error !! the object exists!')
                # raise forms.ValidationError("Exists already!")

            create_obj = PropertType.objects.create(
                name = name,
                notes = notes
                )
            response_data['name'] = create_obj.name
            response_data['notes'] = create_obj.notes
            response_data['created_date'] = create_obj.created_date
            response_data['updated_date'] = create_obj.updated_date
            
            # print("This is the response data ---------------------><><> create_obj.latest", create_obj.created_date)
            return JsonResponse(response_data)
        else:
            err = form.errors.as_json()
            print("ERROR -----><><<  >> form.response", err)
            # return JsonResponse(form.errors.as_json(), status=400,safe=False)
            return JsonResponse({"error": form.errors}, status=400,safe=False)


    
    return render(request,"properties/property-type.html",  {'property_types':property_types})        
