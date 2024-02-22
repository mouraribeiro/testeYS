from django.urls import path, include

from trees.views import *

urlpatterns = [
    path('register/', SingUp.as_view(), name='singup'),
    path('', Plant_list, name='plantlist'),
    path('plant/<int:id>/', PlantView, name='plant list'),
    path('create/', plant_tree, name='create plant'),
    path('json/', plants_json, name='json plant'),

]
