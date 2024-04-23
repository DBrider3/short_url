"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Short URL Url
"""

# System
from django.urls import path, include

# Project
from app.shortlinks.views import ShortURLViewSet

shortlinks_urls = [
    path("", ShortURLViewSet.as_view({"post": "generate_short_url"})),
    path(
        "<int:short_url_id>",
        ShortURLViewSet.as_view({"delete": "delete_user_short_url"}),
    ),
    path("redirect", ShortURLViewSet.as_view({"post": "redirect_short_url"})),
    path("info", ShortURLViewSet.as_view({"get": "get_user_short_url"})),
]

urlpatterns = [
    path("shorturl/", include(shortlinks_urls)),
]
