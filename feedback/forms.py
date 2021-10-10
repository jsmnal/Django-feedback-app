from django import forms
from . import models

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ["course", "rating","feedback",]

class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ["first_name", "last_name",]

class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ["title", "teacher",]

class BugForm(forms.ModelForm):
    class Meta:
        model = models.Bug
        fields = ["title", "message",]
