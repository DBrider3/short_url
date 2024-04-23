"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Project Constants
"""

# System
import os
from dotenv import load_dotenv


load_dotenv()


class SERVICE:
    """
    Service Config
    """

    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = bool(os.getenv("DEBUG", False))
    ACCESS_TOKEN_EXP_MIN = int(os.getenv("ACCESS_TOKEN_EXP_MIN"))
    REFRESH_TOKEN_EXP_DAY = int(os.getenv("REFRESH_TOKEN_EXP_DAY"))


class DATABASE:
    """
    Database Config
    """

    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")


class SYSTEM_CODE:
    """
    각종 System Code
    """

    # 0~1000 Base
    SUCCESS = (0, "SUCCESS")
    BAD_REQUEST = (1, "BAD_REQUEST")
    CLIENT_ERROR = (2, "CLIENT_ERROR")
    INVALID_FORMAT = (3, "INVALID_FORMAT")

    # 1001 ~ 2000 Auth
    EMAIL_ALREADY = (1001, "EMAIL_ALREADY")
    USER_NOT_FOUND = (1002, "USER_NOT_FOUND")
    USER_INVALID_PW = (1003, "USER_INVALID_PW")
    USER_NOT_ACTIVE = (1004, "USER_NOT_ACTIVE")
