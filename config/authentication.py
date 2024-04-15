"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Custom JWT
"""

# System
import jwt
from datetime import datetime, timezone, timedelta
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

# Project
from core.constants import SERVICE
from app.users.models import User


class CustomJWTAuthentication(BaseAuthentication):
    """
    Custom JWT 인증에 관한 부분이므로, 인증시 해당 로직을 처리합니다.
    """

    def authenticate(self, request):
        authorization_header: str = request.headers.get("Authorization", None)

        if not authorization_header:
            return None

        access_token = authorization_header.split(" ")[-1]

        if not access_token:
            return None

        try:
            decoded = jwt.decode(access_token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded.get("id")

            if not user_id:
                raise AuthenticationFailed("Invalid Token")

            user = User.objects.get(id=user_id)
            return (user, None)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.DecodeError:
            raise AuthenticationFailed("Error decoding token")
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")


def create_token(user: User, type):
    """
    access, refresh token 생성하는 함수 입니다.
    """
    if type == "access":
        exp = datetime.now(tz=timezone.utc) + timedelta(minutes=SERVICE.ACCESS_TOKEN_EXP_MIN)
    elif type == "refresh":
        exp = datetime.now(tz=timezone.utc) + timedelta(days=SERVICE.REFRESH_TOKEN_EXP_DAY)

    payload = {
        "user_id": user.id,
        "email": user.email,
        "exp": exp,
        "iat": datetime.now(tz=timezone.utc),
    }

    token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256")
    return token
