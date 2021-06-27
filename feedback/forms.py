from django import forms
from . import models

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ["title", "teacher", "rating","feedback",]

class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ["first_name", "last_name",]
