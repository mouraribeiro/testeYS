from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    about = models.TextField(max_length=500)
    joined = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Account(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Tree(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# aqui seria melhor geofield
class Location(models.Model):
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.lon) + ' , ' + str(self.lat)

class Plant(models.Model):
    age = models.IntegerField()
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.tree.name


