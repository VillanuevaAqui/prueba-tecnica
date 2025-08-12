from rest_framework.test import APITestCase
from rest_framework import status
from .models import Producto

# Pruebas automaticas para validar cada endpoint de la API

class ProductoAPITest(APITestCase):
    def setUp(self):
        self.list_url = '/api/productos/'
        self.product = Producto.objects.create(
            nombre='Producto Test',
            descripcion='Descripción Test',
            precio='100.00',
            disponible=True
        )

    def test_list_productos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_producto(self):
        data = {
            'nombre': 'Nuevo Producto',
            'descripcion': 'Descripción',
            'precio': '50.00',
            'disponible': True
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nombre'], data['nombre'])

    def test_retrieve_producto(self):
        response = self.client.get(f'{self.list_url}{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.product.nombre)

    def test_update_producto(self):
        data = {
            'nombre': 'Producto Modificado',
            'descripcion': 'Nueva descripción',
            'precio': '200.00',
            'disponible': False
        }
        response = self.client.put(f'{self.list_url}{self.product.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.nombre, data['nombre'])
        self.assertFalse(self.product.disponible)

    def test_delete_producto(self):
        response = self.client.delete(f'{self.list_url}{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Producto.objects.filter(id=self.product.id).exists())
