from django.shortcuts import render, redirect
from . import models
from . import forms
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg

def index(request):
    return render(request, "index.html")

@login_required
def statistics(request):
    labels = []
    data = []
    queryset = models.Message.objects.values("course__title").annotate(course_rating=Avg("rating")).order_by("course")
    for message in queryset:
        labels.append(message["course__title"])
        data.append(message["course_rating"])
    return render(request, "statistics.html", {"labels":labels, "data":data})

@login_required
def feedback(request):
    feedback_list = models.Message.objects.order_by("rating")
    context = { "feedback_list": feedback_list }
    return render(request, "feedback.html", context)

@login_required
def teacher(request):
    teacher_list = models.Teacher.objects.order_by("last_name")
    context = {"teacher_list":teacher_list}
    return render(request, "teachers.html", context)

@login_required
def course(request):
    course_list = models.Course.objects.order_by("teacher")
    context = {"course_list": course_list }
    return render(request, "courses.html", context)

@login_required
def bug(request):
    bug_list = models.Bug.objects.order_by("title")
    context = {"bug_list": bug_list }
    return render(request, "bugs.html", context)


def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "sign_in.html", {"form" : form})

@login_required
def sign_out(request):
    logout(request)
    return redirect("index")


class CreateFeedbackForm(LoginRequiredMixin,CreateView):
    model = models.Message
    form_class = forms.FeedbackForm
    template_name = "create_feedback.html"
    success_url = reverse_lazy("feedback")

class DeleteFeedbackForm(LoginRequiredMixin,DeleteView):
    model = models.Message
    form_class = forms.FeedbackForm
    template_name = "delete_feedback.html"
    success_url = reverse_lazy("feedback")

class UpdateFeedbackForm(LoginRequiredMixin,UpdateView):
    model = models.Message
    form_class = forms.FeedbackForm
    template_name = "update_feedback.html"
    success_url = reverse_lazy("feedback")

class CreateTeacherForm(LoginRequiredMixin,CreateView):
    model = models.Teacher
    form_class = forms.TeacherForm
    template_name = "create_teacher.html"
    success_url = reverse_lazy("teachers")

class DeleteTeacherForm(LoginRequiredMixin,DeleteView):
    model = models.Teacher
    form_class = forms.TeacherForm
    template_name = "delete_teacher.html"
    success_url = reverse_lazy("teachers")

class UpdateTeacherForm(LoginRequiredMixin,UpdateView):
    model = models.Teacher
    form_class = forms.TeacherForm
    template_name = "update_teacher.html"
    success_url = reverse_lazy("teachers")

class CreateCourseForm(LoginRequiredMixin,CreateView):
    model = models.Course
    form_class = forms.CourseForm
    template_name = "create_course.html"
    success_url = reverse_lazy("courses")

class DeleteCourseForm(LoginRequiredMixin,DeleteView):
    model = models.Course
    form_class = forms.CourseForm
    template_name = "delete_course.html"
    success_url = reverse_lazy("courses")

class UpdateCourseForm(LoginRequiredMixin,UpdateView):
    model = models.Course
    form_class = forms.CourseForm
    template_name = "update_course.html"
    success_url = reverse_lazy("courses")

class CreateBugForm(LoginRequiredMixin,CreateView):
    model = models.Bug
    form_class = forms.BugForm
    template_name = "create_bug.html"
    success_url = reverse_lazy("bugs")

class DeleteBugForm(LoginRequiredMixin,DeleteView):
    model = models.Bug
    form_class = forms.BugForm
    template_name = "delete_bug.html"
    success_url = reverse_lazy("bugs")

class UpdateBugForm(LoginRequiredMixin,UpdateView):
    model = models.Bug
    form_class = forms.BugForm
    template_name = "update_bug.html"
    success_url = reverse_lazy("bugs")
