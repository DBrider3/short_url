"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Exceptions
"""

# System
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

# Project
from core.constants import SYSTEM_CODE
from core.response import create_response


def custom_exception_handler(exc, context):
    """
    Exception Handler
    예상 못하지 에러는 기본적으로 핸들러로 관리합니다.
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if isinstance(exc, CustomAPIException):
        return response
    if response is not None:
        response.data["status_code"] = response.status_code

    return create_response(
        code=SYSTEM_CODE.UNKNOWN_SERVER_ERROR,
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


class CustomAPIException(APIException):
    """
    Custom APIException
    사용자가 지정하는 에러는 이것으로 전체적으로 관리합니다.
    """

    def __init__(self, **kwargs):
        status_code = kwargs.get("status", 400)
        code = kwargs.get("code", SYSTEM_CODE.BAD_REQUEST)
        detail = code[1]

        data = {
            "data": [],
            "status_code": status_code,
            "msg": detail,
            "code": code[0],
        }
        super().__init__(data, **kwargs)


def raise_exception(**kwargs):
    raise CustomAPIException(**kwargs)
