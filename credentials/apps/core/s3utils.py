"""
Custom S3 storage backends to store files in sub folders.
"""
from functools import partial

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

MediaS3BotoStorage = partial(
    S3Boto3Storage,
    location=settings.MEDIA_ROOT.strip('/')
)

StaticS3BotoStorage = partial(
    S3Boto3Storage,
    location=settings.STATIC_ROOT.strip('/')
)
