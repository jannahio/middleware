# login_jannah/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/login/(?P<workflow_name>\w+)/$", consumers.LoginWithGoogleConsumer.as_asgi()),
]