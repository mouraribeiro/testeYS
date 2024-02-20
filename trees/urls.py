from django.urls import path, include

from trees.views import *

urlpatterns = [
    path('register/', SingUp.as_view(), name ='singup'),
    path('list/', Plant_list.as_view(), name ='plant list'),
    path('view/', PlantView.as_view(), name ='plant view'),


]

