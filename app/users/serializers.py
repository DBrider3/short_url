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
from config.authentication import create_token
from app.users.models import User


class RegisterSerializer(serializers.Serializer):
    """
    회원가입 시리얼라이저
    """

    email = serializers.EmailField(max_length=255, required=True, label="이메일", write_only=True)
    password = serializers.CharField(max_length=128, required=True, label="패스워드", write_only=True)

    access_token = serializers.CharField(read_only=True, label="엑세스 토큰")
    refresh_token = serializers.CharField(read_only=True, label="리프레쉬 토큰")

    def validate_email(self, value):
        """
        email 중복 검사
        """
        if User.objects.filter(email=value).exists():
            raise_exception(code=SYSTEM_CODE.EMAIL_ALREADY, detail=SYSTEM_CODE.EMAIL_ALREADY[1])
        return value

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]

        user = User.objects.create_user(email=email, password=password)

        access_token = create_token(user=user, type="access")
        refresh_token = create_token(user=user, type="refresh")

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }


class LoginSerializer(serializers.Serializer):
    """
    로그인 시리얼라이저
    """

    email = serializers.EmailField(max_length=255, required=True, label="이메일", write_only=True)
    password = serializers.CharField(max_length=128, required=True, label="패스워드", write_only=True)

    access_token = serializers.CharField(read_only=True, label="엑세스 토큰")
    refresh_token = serializers.CharField(read_only=True, label="리프레쉬 토큰")

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = User.objects.filter(email=email).first()

        # 존재 하지 않는 유저
        if not user:
            raise_exception(code=SYSTEM_CODE.USER_NOT_FOUND)

        # 비밀번호 불일치
        if not user.check_password(raw_password=password):
            raise_exception(code=SYSTEM_CODE.USER_INVALID_PW)

        # 활성화 되지 않는 유저
        if not user.is_active:
            raise_exception(code=SYSTEM_CODE.USER_NOT_ACTIVE)

        access_token = create_token(user=user, type="access")
        refresh_token = create_token(user=user, type="refresh")

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
