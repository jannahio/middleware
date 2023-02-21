# login_jannah/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:workflow_name>/", views.with_google, name="with_google"),
]

