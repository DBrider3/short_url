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


class DATABASE:
    """
    Database Config
    """

    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
