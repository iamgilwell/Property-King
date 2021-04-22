from django.urls import path 
from . import views 

app_name = 'properties'

urlpatterns = [
    path('', views.index, name='index')
]
