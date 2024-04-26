"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Root Urls
"""

# System
from django.contrib import admin
from django.urls import path, include

# Project
from app.shortlinks.views import ShortURLViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.users.urls")),
    path("api/", include("app.shortlinks.urls")),
]

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns += [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
