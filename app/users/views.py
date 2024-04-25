"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : User View
"""

# System
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


# Project
from config.authentication import create_token
from core.constants import SYSTEM_CODE
from core.exception import raise_exception
from app.users.models import User
from app.users.serializers import (
    RegisterSerializer,
    LoginSerializer,
)


class AuthViewSet(ViewSet):
    """
    회원가입, 로그인에 관한 ViewSet
    """

    def register(self, request):
        """
        회원가입
        """
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT, detail=SYSTEM_CODE.INVALID_FORMAT[1])

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = User.objects.create_user(email, password)

        access_token = create_token(user=user, type="access")
        refresh_token = create_token(user=user, type="refresh")

        data = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        return Response(data=data, status=status.HTTP_201_CREATED)

    def login(self, request):
        """
        로그인
        """
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT, detail=SYSTEM_CODE.INVALID_FORMAT[1])

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

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

        data = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        return Response(data=data, status=status.HTTP_200_OK)
