from django.test import TestCase
from . import models
# Create your tests here.

class TestCreateTeacher(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = models.User.objects.create_user(username='test', password='test', is_superuser=True, is_staff=True)

    def test_create_teacher_without_auth(self):
        response = self.client.post('/create_teacher/', {'first_name': 'test', 'last_name': 'test'})
        self.assertEqual(models.Teacher.objects.filter(first_name='test', last_name='test').count(), 0)
    
    def test_create_teacher_with_auth(self):
        self.client.login(username='test', password='test')
        response = self.client.post('/create_teacher/', {'first_name': 'test', 'last_name': 'test'})
        self.assertEqual(models.Teacher.objects.filter(first_name='test', last_name='test').count(),1)
