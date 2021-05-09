from django.core.exceptions import ValidationError
from .models import PropertType, PropertyAmenities
from django import forms


class PropertyTypeForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    notes = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    
    def __init__(self, *args, **kwargs):
        super(PropertyTypeForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    def clean(self):
        name = self.data.get('name')
        print('def clean(self) ----><><>< checking name',name )
        if PropertType.objects.filter(name=name).exists():
            raise forms.ValidationError("Property Name Already Exists")
    class Meta:
        model = PropertType
        fields = ("__all__")

class PropertyAmenitiesForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    notes = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    
    def __init__(self, *args, **kwargs):
        super(PropertyAmenitiesForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    def clean(self):
        name = self.data.get('name')
        print('def clean(self) ----><><>< checking name',name )
        if PropertyAmenities.objects.filter(name=name).exists():
            raise forms.ValidationError("Property Amenity Name Already Exists")
    class Meta:
        model = PropertyAmenities
        fields = ("__all__")