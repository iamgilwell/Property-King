from properties.models import PropertyUnits
from django.contrib import admin
from . models import ComplainStatus, ComplainManagement,Tenant, TenantStatus


class CompainStatusAdmin(admin.ModelAdmin):
    list_display = ('name','created_date','updated_date')
admin.site.register(ComplainStatus, CompainStatusAdmin)

class ComplainManagementAdmin(admin.ModelAdmin):
    list_display = ('tenant','notes','complain_file','complain_status','created_date','updated_date')
admin.site.register(ComplainManagement, ComplainManagementAdmin)


class TenantStatusAdmin(admin.ModelAdmin):
    list_display = ('name','created_date','updated_date')
admin.site.register(TenantStatus, TenantStatusAdmin)


class TenantAdmin(admin.ModelAdmin):
    list_display = ('tenant_name','property_unit','tenant_status','tenant_id','tenant_passport','notes','tenant_id_file','tenant_passport_file','created_date','updated_date')
    # search_fields = ["property__property_unit"]
    # list_display_links = ["property", "property_unit"]
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "availability":
    #         parent_id = request.resolver_match.kwargs['object_id']
    #         kwargs["queryset"] = PropertyUnits.objects.filter(availability=True)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "property_unit":
            kwargs["queryset"] = PropertyUnits.objects.filter(availability=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    # def filter_property_by_availability(self,obj):
    #     availability = PropertyUnits.objects.filter(availability=True)
    #     return availability
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     availability = PropertyUnits.objects.filter(availability=True)
    #     # return qs.filter(availability)
    #     return availability
    

admin.site.register(Tenant, TenantAdmin)