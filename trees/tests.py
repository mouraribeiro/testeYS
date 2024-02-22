
from django.test import Client, TestCase
from django.urls import reverse
from .models import Plant, User

# Create your tests here.

# Criar um teste de template que mostre que a listagem de árvores plantadas por um usuário
# específico está sendo renderizada corretamente
class TemplateTest(TestCase):
    #teste do template list que só passa se fizer login do user
    def setUp(self):
        self.user = User.objects.create_user(username='rayanne', password='test_password', is_staff=True)
        self.another_user =  User.objects.create_user(username='teste', password='1234', is_staff=True)
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
    def test_template_forbidden(self):
        self.url = reverse('plantlist')
        self.client.login(username='rayanne', password='test_password')
        # self.another_user.login(username='teste', password='1234')
        response = self.another_user.get(self.url)
        self.assertEqual(403, response.status_code)


class PrivateListTestCase(BaseViewTestCase):

    def setUp(self):
        super(PrivateListTestCase, self).setUp()
        self.url = reverse('plantlist')

    def test_user_sees_own_book(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.first_book.name, response.context['book'].name)
        self.assertTemplateUsed('myapp/book/view_template.html')

    def test_user_cant_see_others_books(self):
        response = self.another_client.get(self.url)
        self.assertEqual(403, response.status_code)







# Criar um teste de template que mostre que a listagem de árvores plantadas pelos usuários das
# contas das quais o usuário é membro está sendo renderizada corretamente


# Criar testes unitários para os métodos User.plant_tree() e User.plant_trees que
# demonstrem que, ao serem chamados, os respectivos objetos Plant são criados e
# associados ao usuário.