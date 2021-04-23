from django.contrib import admin
from .models import Properties, PropertType


class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name','created_date','updated_date')
admin.site.register(PropertType, PropertyTypeAdmin)


class PropertiesTypeAdmin(admin.ModelAdmin):
    list_display = ('name','slug','email','notes','number_of_units','property_type','logo','city','state','contacts','created_date','updated_date')
admin.site.register(Properties, PropertiesTypeAdmin)
