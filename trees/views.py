from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.serializers import serialize
import json
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import CreatePlantForm
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

class PlantCreate(CreateView):
    model = Plant
    template_name = 'plant/create_plant.html'
    form_class = CreatePlantForm
    success_message = "Criado com sucesso!"
    success_url = reverse_lazy('create-plant')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlantCreate, self).form_valid(form)


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


def plants_json(request):
    plant = Plant.objects.all()
    serialized_data = serialize("json", plant)
    serialized_data = json.loads(serialized_data)
    serialized_data

    return JsonResponse(serialized_data, safe=False, status=200)