"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : User Url
"""

# System
from django.urls import path, include

# Project
from app.users.views import (
    RegisterView,
)

auth_urls = [path("", view=RegisterView.as_view())]

urlpatterns = [
    path("auth/", include(auth_urls)),
]
