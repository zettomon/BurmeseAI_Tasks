from django.urls import path
from . import views

urlpatterns = [
    path('', views.submission_portal, name="submission_portal"),
    path('form_add', views.form_add, name="form_add")
]