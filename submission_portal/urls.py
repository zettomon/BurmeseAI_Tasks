from django.urls import path
from . import views

urlpatterns = [
    path('', views.submission_portal, name="submission_portal"),
    path('form_add', views.form_add, name="form_add"),
    path('form_filter_category', views.form_filter_category, name="form_filter_category"),
    path('search_result', views.form_search, name="form_search"),
    path('handle_reviewed', views.handle_reviewed, name="handle_reviewed")
]