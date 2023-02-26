# Django
from django.contrib.auth.hashers import make_password
from django.test import TestCase

# Local
from .forms import ClientForm
from .models import Client


class ClientTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        password = '123'
        Client.objects.create(
            email='user@mail.cc',
            password=make_password(
                password
            ),
            balance=100
        )

    def setUp(self):
        pass

    def test_client_form(self):
        client = Client.objects.get(id=1)
        password = make_password('123')
        data = {
            'email': client.email,
            'password': password,
            'password2': password
        }
        form = ClientForm(data=data)
        self.assertTrue(form.is_valid())