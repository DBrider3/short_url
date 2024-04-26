"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : User Model
"""

# System
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Project
from core.models import BaseModel


class UserManager(BaseUserManager):
    """
    사용자 모델 관리자로, 사용자 생성 및 관리를 처리합니다.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        이메일, 비밀번호 및 추가 필드를 사용하여 새로운 사용자를 생성하고 변환합니다.

        이메일이 제공되지 않을 경우 ValueError를 발생시킵니다.
        """

        if not email:
            raise ValueError("이메일 주소를 필수로 가져야 합니다.")

        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password=None):
        """
        Create and return a new superuser.
        """

        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    """
    시스템 내 개발, 사용자를 나타내는 사용자 모델입니다.
    """

    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="사용자 이메일 주소",
    )
    is_active = models.BooleanField(default=True, verbose_name="활성 사용자 여부")
    is_staff = models.BooleanField(default=False, verbose_name="어드민 여부")

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        app_label = "users"
        db_table = "users"

    def __str__(self) -> str:
        return self.email
