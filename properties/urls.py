from django.urls import path 
from . import views 

app_name = 'properties'

urlpatterns = [
    path('', views.index, name='index'),
    path('property-types/', views.property_types, name='property-types'),
    path('save-property-types/', views.save_property_type, name='save-property-types'),
    path('property-ammenities/', views.property_ammenities, name='property-ammenities')
]
