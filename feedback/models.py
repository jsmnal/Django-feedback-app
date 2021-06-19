from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Message(models.Model):
    title = models.CharField('title', max_length=100)
    teacher = models.ForeignKey('Teacher', verbose_name='teacher', on_delete = models.SET_NULL, null=True)
    rating = models.IntegerField('rating')
    feedback = models.CharField('feedback', max_length=300)


class Teacher(models.Model):
    first_name = models.CharField('first_name', max_length=100)
    last_name = models.CharField('last_name', max_length=100)

class User(AbstractUser):
    pass

    
