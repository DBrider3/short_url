"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : User View
"""

# System
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


# Project
from core.constants import SYSTEM_CODE
from core.exception import raise_exception
from core.response import create_response
from app.users.serializers import (
    RegisterSerializer,
    LoginSerializer,
)


@extend_schema(
    tags=["Auth"],
)
class AuthViewSet(ViewSet):
    """
    회원가입, 로그인에 관한 ViewSet
    """

    @extend_schema(
        summary="회원가입",
        request=RegisterSerializer,
        responses={status.HTTP_201_CREATED: RegisterSerializer},
    )
    def register(self, request):
        """
        회원가입 로직을 처리합니다.
        """
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT, detail=SYSTEM_CODE.INVALID_FORMAT[1])

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        summary="로그인",
        request=LoginSerializer,
        # responses={status.HTTP_200_OK: TokenResponseSerializer},
    )
    def login(self, request):
        """
        로그인 로직을 처리합니다.
        """
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            raise_exception(status=status.HTTP_400_BAD_REQUEST, code=SYSTEM_CODE.INVALID_FORMAT)

        return create_response(data=serializer.data, status=status.HTTP_200_OK)
