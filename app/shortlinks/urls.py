"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Short URL Url
"""

from django.urls import path, include

shortlinks_urls = []

urlpatterns = [
    path("shorturl/", include(shortlinks_urls)),
    path(
        "",
    ),
]
