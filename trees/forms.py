from django import forms
from django.forms import formset_factory

from .models import Plant, Tree, Location, Account


class CreatePlantForm(forms.ModelForm):
    age = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Age', 'class': 'form-control'}
    ))

    # planted_at = forms.IntegerField(
    #     widget=forms.DateTimeInput(
    #         attrs={'placeholder': 'Enter Date', 'class': 'form-control'}
    # ))
    account = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ))

    tree = forms.ModelChoiceField(
        queryset=Tree.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
    ))

    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
    ))

    class Meta:
        model = Plant
        fields = ['age', 'tree', 'location','account']


PlantFormset = formset_factory(CreatePlantForm, extra=3)