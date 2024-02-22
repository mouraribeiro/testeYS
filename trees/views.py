from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView

from .forms import PlantForm, LocationForm
from .models import *


# Create your views here.
class SingUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required
def Plant_list(request):
    planted_tree_list = Plant.objects.all()
    return render(request, 'plant/list.html', {'tree': planted_tree_list})


@login_required
def PlantView(request, id):
    planted_tree = get_object_or_404(Plant, pk=id)
    return render(request, 'plant/view.html', {'plant': planted_tree})


@login_required
def plant_tree(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        form_location = LocationForm(request.POST)

        if form.is_valid():
            plant = form.save(commit=False)
            local = form_location.save(commit=False)
            plant.save()
            local.save()
            return HttpResponse('DEu bom')
        form = PlantForm()
        return render(request, 'plant/create_plant.html', {'form': form})


# metodo para add vários objetos
@login_required
def plant_trees(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)

        if form.is_valid():
            plant = form.save(commit=False)
            plant.save()
            return redirect('/')
    else:
        form = PlantForm()
        return render(request, 'plant/create_plant.html', {'form': form})


from django.http import JsonResponse


def plants_json(request):
    # do something with the your data

    pass
