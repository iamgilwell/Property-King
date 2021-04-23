from django.db import models

class PropertType(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Properties(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    email = models.EmailField(max_length=75)
    notes = models.TextField(max_length=2048*4)
    number_of_units = models.CharField(max_length=255)
    property_type = models.ForeignKey(PropertType, verbose_name=("Propert Type"), on_delete=models.CASCADE)
    logo = models.ImageField(upload_to = "property_logos/")
    city  =  models.CharField(max_length=255)
    state  =  models.CharField(max_length=255)
    contacts =  models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    