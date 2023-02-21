# login_jannah/views.py
from django.shortcuts import render


def index(request):
    return render(request, "login_jannah/index.html")

def with_google(request, workflow_name):
    return render(request, "login_jannah/with_google.html", {"workflow_name": workflow_name})