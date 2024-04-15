"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Custom API Exception
"""

# System
from rest_framework import status
from rest_framework.exceptions import APIException

# Project
from core.constants import SYSTEM_CODE


class CustomAPIException(APIException):
    """
    예상하지 못한 에러는 이것으로 전체적으로 관리합니다.
    Custom APIException
    """

    def __init__(self, **kwargs):
        self.status_code = kwargs.get("status", status.HTTP_400_BAD_REQUEST)
        self.code = kwargs.get("code", SYSTEM_CODE.CLIENT_ERROR)
        self.detail = kwargs.get("detail", "오류가 발생했습니다.")


def raise_exception(**kwargs):
    raise CustomAPIException(**kwargs)
