# Python
from typing import Any

# Django
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.base import ModelBase
from django.db.models.signals import (
    post_delete,
    post_save
)
# from django.dispatch import receiver

# First party
from abstracts.utils import get_eta_time

# Local
# from .tasks import sending
from auths.models import Client


# @receiver(
#     post_save,
#     sender=Player
# )
# def post_save_player(
#     sender: ModelBase,
#     instance: Player,
#     created: bool,
#     **kwargs: Any
# ) -> None:
#     """Post-save Player."""
#     if created:
#         notify.apply_async(
#             args=('Created', instance.fullname, str(instance)),
#             eta=get_eta_time(3)
#         )
#         return


# @receiver(
#     post_save,
#     sender=Client
# )
# def post_save_user(
#     sender: ModelBase,
#     instance: Client,
#     created: bool,
#     **kwargs: Any
# ):
#     """Post-save ClientManager"""
#     if created:
#         sending.apply_async(
#             args=('Created', instance.email),
#             eta=get_eta_time(5)
#         )
#         return