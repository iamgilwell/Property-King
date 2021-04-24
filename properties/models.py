from django.db import models
from django.contrib.gis.db import models


def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/unit_images/{filename}'
class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/unit_images/%Y/%m/%d/")
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    # album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)

class PropertType(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PropertyAmenities(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Property Amenities'
        verbose_name_plural= 'Property Amenities'
    
class Properties(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    email = models.EmailField(max_length=75)
    notes = models.TextField(max_length=2048*4)
    number_of_units = models.CharField(max_length=255)
    property_value = models.DecimalField(max_length=255,max_digits=5, decimal_places=2, null=True, blank=True)
    property_type = models.ForeignKey(PropertType, verbose_name=("Propert Type"), on_delete=models.CASCADE)
    property_ammenities = models.ManyToManyField(PropertyAmenities, verbose_name=("Propert Amenities"))
    location_map =models.MultiPolygonField(srid=4326, null=True, blank=True)
    logo = models.ImageField(upload_to = "property_logos/")
    city  =  models.CharField(max_length=255)
    state  =  models.CharField(max_length=255)
    contacts =  models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Properties'
        verbose_name_plural= 'Properties'

class PropertyUnits(models.Model):
    property = models.ForeignKey(Properties, verbose_name=("Property"), on_delete=models.CASCADE)
    unit_name =  models.CharField(max_length=255)
    unit_number =  models.CharField(max_length=255)
    price =  models.DecimalField(max_length=255,max_digits=5, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    master_ensuite = models.BooleanField(default="NO")
    notes = models.TextField(max_length=2048*4)
    photos = models.ManyToManyField(Image, related_name='images')
    created_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.unit_name
    class Meta:
        verbose_name = 'Property Units'
        verbose_name_plural= 'Property Units'
    
    