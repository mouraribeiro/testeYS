
from django.test import Client, TestCase
from django.urls import reverse
from .models import Plant

# Create your tests here.

# Criar um teste de template que mostre que a listagem de árvores plantadas por um usuário
# específico está sendo renderizada corretamente

class TestPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_list_page(self):
        url = reverse('plantlist')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'plantlist')
        self.assertContains(response, 'Lista de Plantas')

# class HomepageTests(SimpleTestCase):
#     def test_url_exists_at_correct_location(self):
#         response = self.client.get("/")
#         self.assertEqual(response.status_code, 200)
# Criar um teste de template que mostre que ao tentar acessar as árvores plantadas por outro
# usuário é retornado um erro 403 (Forbidden).

# Criar um teste de template que mostre que a listagem de árvores plantadas pelos usuários das
# contas das quais o usuário é membro está sendo renderizada corretamente


# Criar testes unitários para os métodos User.plant_tree() e User.plant_trees que
# demonstrem que, ao serem chamados, os respectivos objetos PlantedTree são criados e
# associados ao usuário.