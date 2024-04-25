"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Cron tab for handling expired short URLs
"""

# System
from datetime import datetime

# Project
from app.shortlinks.models import Shortlink


def handle_expired_shortlinks():
    """
    단축 url 00시에 만료된것들 삭제 처리한다.
    """
    # 현재 시간 기준으로 만료된 shortlink 객체를 찾습니다.
    expired_links = Shortlink.objects.filter(deleted_at=None, expiration_date__lt=datetime.now())

    # 각 만료된 객체에 대해 deleted_at을 현재 시간으로 설정
    for link in expired_links:
        link.deleted_at = datetime.now()
        link.save()
        print(f"Processed expired link: {link.url}")

    # 로그 또는 콘솔 출력을 통해 처리된 만료 링크 수를 알림
    print(f"Total {expired_links.count()} expired links processed.")
