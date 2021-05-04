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

    class Meta:
        model = PropertType
        fields = ("__all__")