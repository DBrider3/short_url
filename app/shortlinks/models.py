"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Short URL Model
"""

# System
from django.db import models

# Project
from core.models import BaseModel


class Shortlink(BaseModel):
    url = models.URLField(verbose_name="url")
    encoded = models.CharField(max_length=100, verbose_name="Short url")
    expiration_date = models.DateTimeField(null=True, blank=True, verbose_name="만료일시")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="삭제일시")

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="shortlink_user",
    )

    class Meta:
        app_label = "shortlinks"
        db_table = "shortlinks"
