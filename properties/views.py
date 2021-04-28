from django.shortcuts import render
from . models import Properties
# Create your views here.

def index(request):
    properties = Properties.objects.all()
    context  = {
        'properties':properties
    }
    return render(request,"properties/index.html", context)