from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class RegisterViewTests(APITestCase):
    def test_registro_con_datos_validos_crea_usuario(self):
        url = reverse('register')
        data = {
            'email': 'nuevo@ejemplo.com',
            'name': 'Ana',
            'surname': 'García',
            'username': 'anagarcia',
            'password': 'contraseñaSegura123',
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='nuevo@ejemplo.com').exists())

    def test_registro_sin_email_devuelve_400(self):
        url = reverse('register')
        data = {
            'name': 'Ana',
            'surname': 'García',
            'username': 'anagarcia',
            'password': 'contraseñaSegura123',
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='mariaperez',
            email='maria@ejemplo.com',
            name='María',
            surname='Pérez',
            password='miContraseña123',
        )

    def test_login_con_credenciales_correctas(self):
        url = reverse('login')
        data = {'email': 'maria@ejemplo.com', 'password': 'miContraseña123'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['email'], 'maria@ejemplo.com')

    def test_login_con_contraseña_incorrecta_devuelve_401(self):
        url = reverse('login')
        data = {'email': 'maria@ejemplo.com', 'password': 'contraseñaMala'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_sin_password_devuelve_400(self):
        url = reverse('login')
        data = {'email': 'maria@ejemplo.com'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='mariaperez',
            email='maria@ejemplo.com',
            name='María',
            surname='Pérez',
            password='miContraseña123',
        )

    def test_listar_usuarios_sin_autenticar_devuelve_401(self):
        url = reverse('users')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_listar_usuarios_autenticado_devuelve_200(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('users')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)