"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : User Url
"""

from django.urls import path, include

auth_urls = []

urlpatterns = [
    path("auth/", include(auth_urls)),
]
