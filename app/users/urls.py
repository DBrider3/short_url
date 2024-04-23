"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : User Url
"""

# System
from django.urls import path, include

# Project
from app.users.views import AuthViewSet

auth_urls = [
    path("", view=AuthViewSet.as_view({"post": "login"})),
    path("registration", view=AuthViewSet.as_view({"post": "register"})),
]

urlpatterns = [
    path("auth/", include(auth_urls)),
]
