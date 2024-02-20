from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()
    active = models.BooleanField()
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


# class User(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user


class Profile(models.Model):
    about = models.TextField(max_length=500)
    joined = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Tree(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PlantedTree(models.Model):
    age = models.IntegerField()
    planted_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)


    def location(self):
        pass
