from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from .models import *


# Create your views here.
class SingUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def Plant_list(request):
    planted_tree_list = Plant.objects.all()
    return render(request, 'plant/list.html', {'tree': planted_tree_list})


def PlantView(request, id):
    planted_tree = get_object_or_404(Tree, pk=id)
    return render(request, 'plant/view.html', {'tree': planted_tree})

