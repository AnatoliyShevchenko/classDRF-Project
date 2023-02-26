# Python
from typing import Any

# Django
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

# First party
from settings.celery import app

# Local
from .models import Player, PlayerManager


# @app.task(
#     name='change-player-age'
# )
# def change_player_age(*args: Any) -> None:
#     for player in Player.objects.all():
#         current_age: int = player.age
#         player.age = current_age + 1
#         try:
#             player.save(update_fields=('age',))
#             print(f'Player: {player.id} success')
#         except ValidationError:
#             print(f'Player: {player.id} failed')

#     print('CALLED: CHANGE PLAYER AGE')

# @app.task(
#     name='sending-raport'
# )
# def sending_raport():
#     players_data = Player.objects.filter(status=0)
#     players = []
#     for player in players_data:
#         temp = f'{player.name} {player.surname} {player.power}'
#         players.append(temp)
#     send_mail(
#         'New Players',
#         f'Free Agents: {players}',
#         settings.EMAIL_HOST_USER,
#         ['metallugabns@yandex.kz'],
#         fail_silently=False
#     )
#     print('CALLED: sending raport')

# @app.task
# def notify(*args: Any) -> None:
#     if args[0] == 'Created':
#         send_mail(
#             f'Новый игрок: {args[1]}',
#             f'Доступен новый игрок на трансферном рынке: {args[2]}',
#             settings.EMAIL_HOST_USER,
#             ['metallugabns@yandex.kz'],
#             fail_silently=False
#         )
#     elif args[0] == 'FreeAgent':
#         send_mail(
#             f'Свободный агент: {args[1]}',
#             f'Доступен игрок на трансферном рынке: {args[2]}',
#             settings.EMAIL_HOST_USER,
#             ['metallugabns@yandex.kz'],
#             fail_silently=False
#         )
#     elif args[0] == 'Retired':
#         send_mail(
#             f'Завершил карьеру: {args[1]}',
#             f'Игрок завершил карьеру: {args[2]}',
#             settings.EMAIL_HOST_USER,
#             ['metallugabns@yandex.kz'],
#             fail_silently=False
#         )
#     print('CALLED: NOTIFY')

# @app.task
# def sending(*args: Any):
#     players_data = Player.objects.filter(status=0)
#     players = []
#     for player in players_data:
#         temp = f'{player.name} {player.surname} {player.power}'
#         players.append(temp)
#     if args[0] == 'Created':
#         send_mail(
#             'YOU JERK',
#             f'You jerk',
#             settings.EMAIL_HOST_USER,
#             ['metallugabns@yandex.kz'],
#             fail_silently=False
#         )
#     print('CALLED: sending')