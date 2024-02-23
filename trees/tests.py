import datetime
from datetime import timezone
from http import HTTPStatus

from django.contrib.sites import requests
from django.http import response
from django.test import Client, TestCase
from django.urls import reverse
from .models import User, Plant, Tree, Account, Location


# Create your tests here.

# Criar um teste de template que mostre que a listagem de árvores plantadas por um usuário
# específico está sendo renderizada corretamente
class TemplateTest(TestCase):
    #teste do template list que só passa se fizer login do user
    def setUp(self):
        self.user = User.objects.create_user(username='rayanne', password='test_password', is_staff=True)
        self.another_user = User.objects.create_user(username='teste', password='1234', is_staff=True)

        self.user.save()
        self.another_user.save()
        self.user = Client()
        self.another_user = Client()
    def test_template_list(self):
        self.client.login(username='rayanne', password='test_password')
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'plant/list.html')
        self.assertTemplateUsed(response, 'base.html')



class TestPermission(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='rayanne', password='test_password', is_staff=True)
        self.another_user = User.objects.create_user(username='teste', password='1234', is_staff=True)

        self.user.save()
        self.another_user.save()
        self.user = Client()
        self.another_user = Client()

# Criar um teste de template que mostre que ao tentar acessar as árvores plantadas por outro
# usuário é retornado um erro 403 (Forbidden).
    def test_forbidden(self):
        self.client.login(username='rayanne', password='test_password')
        self.another_user.login(username='teste', password='1234')
        request_user = self.another_user
        url_base = 'http://127.0.0.1:8000/'
        if request_user.get(url_base) == self.another_user:
            return self.assertEqual(403, response.status_code)



class PostPlantViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='rayanne', password='test_password', is_staff=True)
        self.user.save()
        self.user = Client()

    def test_get(self):
        response = self.client.get("/create/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<title> Plantas </title>", html=True)

    def test_post_success(self):
        self.user = User.objects.create_user(username='teste', password='test_password', is_staff=True)
        tree = Tree.objects.create(name="planta1",scientific_name='plants')
        account = Account.objects.create(name="Conta-1",created=datetime.datetime.now(),active=True)
        location = Location.objects.create(lon=00.02584, lat=00.02584)

        plant = Plant.objects.create(planted_at=datetime.datetime.now(), age= 2, user= self.user, tree= tree, location=location,account=account)
        self.assertEqual(plant.age, 2)
        self.assertEqual(plant.account, account)

