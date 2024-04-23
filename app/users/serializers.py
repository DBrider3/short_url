"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : User Serializers
"""

# System
from rest_framework import serializers, status

# Project
from core.constants import SYSTEM_CODE
from core.exception import raise_exception
from app.users.models import User


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=128, required=True)

    def validate_email(self, value):
        """
        email 중복 검사
        """
        if User.objects.filter(email=value).exists():
            raise_exception(code=SYSTEM_CODE.EMAIL_ALREADY, detail=SYSTEM_CODE.EMAIL_ALREADY[1])
        return value


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=128, required=True)
