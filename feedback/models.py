from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Message(models.Model):
    title = models.CharField('title', max_length=100)
    course = models.ForeignKey('Course', verbose_name='course', on_delete = models.SET_NULL, null=True)
    teacher = models.ForeignKey('Teacher', verbose_name='teacher', on_delete = models.SET_NULL, null=True)
    rating = models.IntegerField('rating')
    feedback = models.CharField('feedback', max_length=300)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    title = models.CharField('title', max_length=100)
    teacher = models.ForeignKey('Teacher', verbose_name='teacher', on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.teacher}/{self.title}"

class Bug(models.Model):
    title = models.CharField('title', max_length=100)
    message = models.CharField('message', max_length=300)

    def __str__(self):
        return self.title

class User(AbstractUser):
    pass

    
