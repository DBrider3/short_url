"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Short URL Serializers
"""

# System
from rest_framework import serializers, status

# Project
from core.constants import SYSTEM_CODE
from core.exception import raise_exception
from app.shortlinks.models import Shortlink


class GenerateSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)
    expiration_date = serializers.DateTimeField(required=False)


class RedirectSerializer(serializers.Serializer):
    encoded = serializers.CharField(max_length=100, required=True)


class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortlink
        fields = ["url", "encoded", "expiration_date"]
