from django.core.exceptions import ValidationError
from .models import PropertType
from django import forms


class PropertyTypeForm(forms.ModelForm):
    ## change the widget of the date field.
    name = forms.CharField(max_length=100)
    notes = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    
    def __init__(self, *args, **kwargs):
        super(PropertyTypeForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    def clean(self):
        name = self.data.get('name')
        print('def clean(self) ----><><>< checking name',name )
        if PropertType.objects.filter(name=name).exists():
            raise forms.ValidationError("Property Name Already Exists")

    # def clean(self):
    #     cleaned_data = super(PropertyTypeForm, self).clean()
    #     name = self.data.get('name')
    #     # print('def clean(self) ----><><>< checking name',name )
    #     obj, created = PropertType.objects.get_or_create(name=name)
    #     print('----######--- def clean(self) ----#### obj', obj)
    #     print('----######--- def clean(self) ----#### created', created)
    #     if created:
    #         print('its a new one, hooray!')
    #     else:
    #         print('the object exists!')
    #         raise forms.ValidationError("Property Name Already Exists")
        # try:
        #     PropertType.objects.get(name=self.cleaned_data['name'] )
        #     #if we get this far, we have an exact match for this form's data
        #     raise forms.ValidationError("Exists already!")
        # except PropertType.DoesNotExist:
        #     #because we didn't get a match
        #     pass

        # return self.cleaned_data
        # return cleaned_data

    class Meta:
        model = PropertType
        fields = ("__all__")