from django import forms

from .models import Plant, Location


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"



class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"


