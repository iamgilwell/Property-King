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

admin.site.register(Tenant, TenantAdmin)