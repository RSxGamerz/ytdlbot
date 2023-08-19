#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - config.py
# 8/28/21 15:01
#

__author__ = "Benny <benny.think@gmail.com>"

import os

# general settings
WORKERS: int = int(os.getenv("WORKERS", 100))
PYRO_WORKERS: int = int(os.getenv("PYRO_WORKERS", min(64, (os.cpu_count() + 4) * 10)))
APP_ID: int = int(os.getenv("APP_ID", 23918516))
APP_HASH = os.getenv("APP_HASH", "44394f47035ffb390840eb9e3c807751")
TOKEN = os.getenv("TOKEN", "6586327242:AAGpN8zwtM78D8hg7Ph1qvTN0FFNbb4KAuU")

REDIS = os.getenv("REDIS", "redis")

TG_MAX_SIZE = 2000 * 1024 * 1024
# TG_MAX_SIZE = 10 * 1024 * 1024

EXPIRE = 24 * 3600

ENABLE_VIP = os.getenv("VIP", False)
AFD_LINK = os.getenv("AFD_LINK", "https://afdian.net/@RXOuO")
COFFEE_LINK = os.getenv("COFFEE_LINK", "https://www.buymeacoffee.com/RX_OuO")
COFFEE_TOKEN = os.getenv("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5MTI5ZDIwMC1kYTdkLTRjY2MtOWQzZC01ODA0MTU0ZTgyMjYiLCJqdGkiOiIxM2I2MzMwNmQwYzhhMDIxODdjMWM4NTY0N2VlOWFhMjljZmU3Yjk5ZjE4ZTYwZTcxNjJmMmYwMWVkODBhOTAwNTE0Mzg5NGRjN2VmMTc0YSIsImlhdCI6MTY5MjQ3NzYzMiwibmJmIjoxNjkyNDc3NjMyLCJleHAiOjE3MDgzNzUyMzIsInN1YiI6IjQxOTIwODUiLCJzY29wZXMiOltdfQ.yVGVQ8-fN95wXXOcvtl7T4-xBXgvN23Z3H5GLx1ZDHFdQcq1jmzjvijPw48xfikqXbF1vNZAyOnNr9dvDc0YoLucGg9owg0pgIsSAL8G5KenPGjwO-temUKIK1jW3BY7YAZTNi5LCjPZdB4gMNkgiheUaW3kaD5QoKGDuSWvYgZiHQPMyD6wyMGR3H1cs73k2XYUXc-ndV6QMZY-gAu-HixHc_DelE4eisjKhsDsFuy7eCXtn-KiLXk43-57u2pvcIEARGT0p3zJKgSoHNXV_oSJALhm9I6KmGANpXIfC3K7ycbpLE52QmBrhGqNdm48IC6_MrE04cb8MYecA-r2ujgtopRs-pSEZINTxYi9eH_Ynq66x80ysen31nXmDu5I2-YAVO4Hr7ARvxNiQnvQB2ks6e302ruPMIB5CO372nOyYVL5gI_QTF6tW90K2PaOgmKAcAlliE_fOR-bHiqPbj2PapzFPiZT8Tjtlf2loqF6ZJgOylxR79fQSFhbTsnKUgA5t5Ydr03bXTAilc5MeuzlRGnDodjiU2FKJYaJEMmGpmzieLxqxokX6COUCIa0bx56qkCTvCx6g-ZGb2oxCiKhhXAUtPj6_ip-kVvzv-rUNOH4fK6OyUPprXVHKCbd55Inj9bgJnIXuo-XoUyZLkgvzygDn2fDfL2J1Ja6qqw")
AFD_TOKEN = os.getenv("ymwWQCnVJutcRSU5qPNrHvpEax4gb3D7")
AFD_USER_ID = os.getenv("RX_OuO")
OWNER = os.getenv("OWNER", "RX_OuO")

# limitation settings
AUTHORIZED_USER: str = os.getenv("AUTHORIZED_USER", "")
# membership requires: the format could be username(without @ sign)/chat_id of channel or group.
# You need to add the bot to this group/channel as admin
REQUIRED_MEMBERSHIP: str = os.getenv("REQUIRED_MEMBERSHIP", "")

# celery related
ENABLE_CELERY = os.getenv("ENABLE_CELERY", False)
ENABLE_QUEUE = os.getenv("ENABLE_QUEUE", False)
BROKER = os.getenv("BROKER", f"redis://{REDIS}:6379/4")

MYSQL_HOST = os.getenv("MYSQL_HOST", "sql212.infinityfree.com")
MYSQL_USER = os.getenv("MYSQL_USER", "if0_34833848")
MYSQL_PASS = os.getenv("MYSQL_PASS", "e7o69E9Uh8tnXh")

AUDIO_FORMAT = os.getenv("AUDIO_FORMAT")
ARCHIVE_ID = os.getenv("ARCHIVE_ID")

IPv6 = os.getenv("IPv6", False)
ENABLE_FFMPEG = os.getenv("ENABLE_FFMPEG", False)

# Stripe setting
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN") or "1234"

PLAYLIST_SUPPORT = os.getenv("PLAYLIST_SUPPORT", False)
ENABLE_ARIA2 = os.getenv("ENABLE_ARIA2", False)

FREE_DOWNLOAD = os.getenv("FREE_DOWNLOAD", 20)
TOKEN_PRICE = os.getenv("BUY_UNIT", 20)  # one USD=20 credits

RATE_LIMIT = os.getenv("RATE_LIMIT", 20)

SS_YOUTUBE = os.getenv("SS_YOUTUBE", "https://ytdlbot.dmesg.app?token=123456")
