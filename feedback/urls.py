from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign_in", views.sign_in, name="sign_in"),
    path("sign_out", views.sign_out, name="sign_out"),
    path("create_feedback/", views.CreateFeedbackForm.as_view(), name="create_feedback"),
    path("delete_feedback/<pk>/", views.DeleteFeedbackForm.as_view(), name="delete_feedback"),
    path("update_feedback/<pk>/", views.UpdateFeedbackForm.as_view(), name="update_feedback"),
    path("create_teacher/", views.CreateTeacherForm.as_view(), name="create_teacher"),
    path("delete_teacher/<pk>/", views.DeleteTeacherForm.as_view(), name="delete_teacher"),
    path("update_teacher/<pk>/", views.UpdateTeacherForm.as_view(), name="update_teacher"),
    path("feedback/", views.feedback, name="feedback"),
    path("teachers/", views.teacher, name="teachers"),
    path("statistics/", views.statistics, name="statistics"),
]