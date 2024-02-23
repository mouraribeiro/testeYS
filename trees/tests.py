from django.contrib.sites import requests
from django.test import Client, TestCase, SimpleTestCase
from django.urls import reverse
from .models import Plant, User, Tree


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

    # Criar um teste de template que mostre que ao tentar acessar as árvores plantadas por outro
    # usuário é retornado um erro 403 (Forbidden).
    # def test_template_forbidden(self):
    #     self.url = reverse('plantlist')
    #     self.client.login(username='rayanne', password='test_password')
    #     # self.another_user.login(username='teste', password='1234')
    #     response = self.another_user.get(self.url)
    #     self.assertEqual(403, response.status_code)

    def test_post_create_view_POST_success(self):
        self.client.login(username='rayanne', password='test_password')
        url_base = 'http://127.0.0.1:8000/multiple/'
        tree = "tree"
        data = {
            "id": 1,
            "age": 2,
            "tree": tree,
            "location": '-19.912998, -43.940933'
        }
        response = self.client.post(url_base, data, content_type="application/x-www-form-urlencoded")
        # response = self.client.post(url_base, data=data,
        #                             follow=True)
        # print(Plant.objects.all()) # make sure your url is correct too btw that could also be the issue
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(Plant.objects.all().last().count(), 1)


