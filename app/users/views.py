"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : User View
"""

# System
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # 권한 부여


# Project
from config.authentication import create_token
from core.constants import SYSTEM_CODE
from core.exception import raise_exception
from app.users.models import User
from app.users.serializers import (
    RegisterSerializer,
)


class RegisterView(APIView):
    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = User.objects.create_user(email, password)

        access_token = create_token(user=user, type="access")
        refresh_token = create_token(user=user, type="refresh")

        data = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        return Response(data=data, status=200)
