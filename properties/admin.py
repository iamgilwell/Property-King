from django.contrib import admin
from .models import Properties, PropertType, PropertyAmenities, PropertyUnits, Image

def get_unit_photos(self, obj):
    return "\n".join([u.name for u in obj.Image.all()])

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','image','default','width','length')
admin.site.register(Image, ImageAdmin)

class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name','created_date','updated_date')
admin.site.register(PropertType, PropertyTypeAdmin)

class PropertyAmenitiesAdmin(admin.ModelAdmin):
    list_display = ('name','created_date','updated_date')
admin.site.register(PropertyAmenities, PropertyAmenitiesAdmin)

class PropertiesTypeAdmin(admin.ModelAdmin):
    list_display = ('name','slug','email','notes','number_of_units','property_type','get_property_ammenities','logo','city','state','contacts','created_date','updated_date')
    def get_property_ammenities(self, obj):
        return "\n".join([u.name for u in obj.property_ammenities.all()])
admin.site.register(Properties, PropertiesTypeAdmin)

class PropertyUnitsAdmin(admin.ModelAdmin):
    list_display = ('property','unit_name','unit_number','price','bedrooms','bathrooms','master_ensuite','notes')
admin.site.register(PropertyUnits, PropertyUnitsAdmin)



