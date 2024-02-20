from django.urls import path, include

from trees.views import home

urlpatterns = [
    path('', home),


]

