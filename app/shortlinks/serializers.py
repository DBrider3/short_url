"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Short URL Serializers
"""

# System
from rest_framework import serializers

# Project
from app.shortlinks.models import Shortlink


class GenerateSerializer(serializers.Serializer):
    url = serializers.URLField(required=True, label="기존 url")
    expiration_date = serializers.DateTimeField(required=False, label="만료기한")


class RedirectSerializer(serializers.Serializer):
    encoded = serializers.CharField(max_length=100, required=True, label="단축url코드")


class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortlink
        fields = ["url", "encoded", "expiration_date"]
