from django.urls import path, include

from trees.views import *

urlpatterns = [
    path('register/', SingUp.as_view(), name ='singup'),
    path('list/', Plant_list, name ='plant list'),
    path('view/', PlantView, name ='plant view'),


]

