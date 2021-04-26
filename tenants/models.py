from django.db import models
from properties.models import Properties, PropertyUnits
from django.core.exceptions import ValidationError


class TenantStatus(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Tenant Status'
        verbose_name_plural= 'Tenant Status'
class Tenant(models.Model):
    tenant_name =  models.CharField(max_length=255)
    property_unit = models.ForeignKey(PropertyUnits, verbose_name=("Property Unit"), on_delete=models.CASCADE)
    tenant_status = models.ForeignKey(TenantStatus, verbose_name=("Tenant Status"), on_delete=models.CASCADE)
    tenant_id =  models.CharField(max_length=255)
    tenant_passport =  models.CharField(max_length=255)
    notes = models.TextField(max_length=2048*4)
    tenant_id_file = models.FileField(blank=True, null=True, upload_to="tenant_id")
    tenant_passport_file = models.FileField(blank=True, null=True, upload_to="tenant_passport")
    created_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.tenant_name
    # def __str__(self):
    #     return "[%s] %s" % (self.property.name, self.property_unit)

    def save(self, *args, **kwargs):
        try:
            self.full_clean()
            print("models, tenant.py -----------", self.property_unit)
            # print("models, tenant.py , self.property", self.property)
            # print("models, tenant.py , self.property_unit", self.property_unit)

            # propery_unit_updt = PropertyUnits.objects.get(id=self.property_unit_id)
            properties = PropertyUnits.objects.filter(unit_name=self.property_unit)
            print("models, tenant.py ----------- properties", properties)
            for item in properties:
                print("models, tenant.py ----------- item", item.property)
            # # check_proprty = PropertyUnits.objects.select_related().filter(property = property, property_unit=self.property_unit)
            # check_property_unit= PropertyUnits.objects.filter(property__property_unit=propery_unit_updt.unit_name)
            # print("models, tenant.py , check_proprty", check_property_unit)

            propery_unit_updt = PropertyUnits.objects.get(id=self.property_unit_id)
            propery_unit_updt.availability = False
            propery_unit_updt.save()

        except ValidationError as e:
            # dont save
            # Do something based on the errors contained in e.message_dict.
            # Display them to a user, or handle them programmatically.
            pass
        else:
            super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'Tenants'
        verbose_name_plural= 'Tenants'


class ComplainStatus(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Complain Status'
        verbose_name_plural= 'Complain Status'
class ComplainManagement(models.Model):
    tenant = models.ForeignKey(Tenant, verbose_name=("Tenant"), on_delete=models.CASCADE)
    notes = models.TextField(max_length=2048*4)
    complain_file = models.FileField(blank=True, null=True, upload_to="tenant_passport")
    complain_status = models.ForeignKey(ComplainStatus, verbose_name=("Complain Status"), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    

    

