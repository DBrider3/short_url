"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Short URL View
"""

# System
import base62
from datetime import datetime
from django.shortcuts import redirect
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated  # 권한 부여
from rest_framework.response import Response
from rest_framework import status

# Project
from core.constants import SYSTEM_CODE
from core.exception import raise_exception
from app.shortlinks.serializers import (
    GenerateSerializer,
    RedirectSerializer,
    ShortURLSerializer,
)
from app.shortlinks.models import Shortlink


class ShortURLViewSet(ViewSet):
    """
    Short URL에 관련된 ViewSet
    """

    permission_classes = [IsAuthenticated]

    def get_user_short_url(self, request):

        user = request.user

        short_url = Shortlink.objects.filter(user=request.user, deleted_at=None).order_by("-created_at")

        serializer = ShortURLSerializer(short_url, many=True)

        data = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)

    def generate_short_url(self, request):

        user = request.user

        serializer = GenerateSerializer(data=request.data)

        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT, detail=SYSTEM_CODE.INVALID_FORMAT[1])

        url = serializer.validated_data["url"]
        expiration_date = serializer.validated_data.get("expiration_date")

        # 회원이 가지고 있는 url이 있는지 확인
        origin_url = Shortlink.objects.filter(url=url, user=user, deleted_at=None).first()
        result_encoded = ""
        if not origin_url:
            new_url = Shortlink.objects.create(url=url, user=request.user)
            new_url.encoded = base62.encode(new_url.id)
            if expiration_date is not None:
                new_url.expiration_date = expiration_date
            new_url.save()
            result_encoded = new_url.encoded
        else:
            origin_url.encoded = base62.encode(origin_url.id)
            if expiration_date is not None:
                origin_url.expiration_date = expiration_date
            origin_url.save()
            result_encoded = origin_url.encoded

        data = {"url": url, "encoded": result_encoded}

        return Response(data=data, status=status.HTTP_201_CREATED)

    def redirect_short_url(self, request):

        serializer = RedirectSerializer(data=request.data)

        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT, detail=SYSTEM_CODE.INVALID_FORMAT[1])

        encoded = serializer.validated_data["encoded"]

        short_url = Shortlink.objects.filter(encoded=encoded, user=request.user, deleted_at=None).first()

        if not short_url:
            raise_exception(
                code=SYSTEM_CODE.SHORT_URL_NOT_FOUND,
                detail=SYSTEM_CODE.SHORT_URL_NOT_FOUND[1],
            )

        return redirect(short_url.url)

    def delete_user_short_url(self, request, short_url_id):

        short_url = Shortlink.objects.filter(user=request.user, deleted_at=None).first()

        if not short_url:
            raise_exception(
                code=SYSTEM_CODE.SHORT_URL_NOT_FOUND,
                detail=SYSTEM_CODE.SHORT_URL_NOT_FOUND[1],
            )

        short_url.deleted_at = datetime.now()
        short_url.save()

        return Response(status=status.HTTP_200_OK)
