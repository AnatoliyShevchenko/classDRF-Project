# Python
from typing import (
    Any,
    Optional
)

# DRF
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Django
from django.db.models.query import QuerySet

# Local
from abstracts.mixins import (
    ObjectMixin,
    ResponseMixin
)
from abstracts.decorators import performance_counter
from .models import Player
from .serializers import (
    PlayerCreateSerializer,
    PlayerSerializer
)
from .permissions import MainPermission


class MainViewSet(ResponseMixin, ObjectMixin, ViewSet):
    """MainViewSet."""

    permission_classes: tuple = (
        MainPermission,
    )
    queryset = Player.objects.all()

    @action(
        methods=['get'],
        detail=False,
        url_path='get-players',
        permission_classes=(AllowAny,)
    )
    def get_players(self, request: Request) -> Response:
        """GET method."""

        players: QuerySet[Player] = \
            self.queryset.filter(power__lte=20)

        serializer: PlayerSerializer = \
            PlayerSerializer(
                players,
                many=True
            )
        return self.get_json_response(serializer.data, 'players')

    @performance_counter
    def list(self, request: Request) -> Response:
        """GET method."""

        players: QuerySet[Player] = self.queryset.all()
        serializer: PlayerSerializer = \
            PlayerSerializer(
                players,
                many=True
            )
        return self.get_json_response(serializer.data, 'players')

    def retrieve(self, request: Request, pk: str) -> Response:
        """GET method."""

        player: Optional[Player] = self.get_object(
            self.queryset,
            pk
        )
        if not player:
            return self.get_json_response('No such player', 'error')
        return self.get_json_response(
            {
                'name': player.name,
                'surname': player.surname,
                'power': player.power,
                'age': player.age
            }
        )

    def create(self, request: Request) -> Response:
        """POST method."""

        serializer: PlayerCreateSerializer = \
            PlayerCreateSerializer(
                data=request.data
            )
        if not serializer.is_valid():
            return self.get_json_response(serializer.errors, 'data')
        player: Player = serializer.save()
        return self.get_json_response(player.fullname, 'players')

    def update(self, request: Request, pk: str) -> Response:
        """POST method."""

        player: Optional[Player] = self.get_object(
            self.queryset,
            pk
        )
        if not player:
            return self.get_json_response('No such player', 'error')
        serializer: PlayerSerializer = PlayerSerializer(
            player,
            data=request.data
        )
        if not serializer.is_valid():
            return self.get_json_response(serializer.errors, 'error')
        serializer.save()
        return self.get_json_response('Updated', 'success')

    def partial_update(self, request: Request, pk: str) -> Response:
        """POST method."""

        player: Optional[Player] = self.get_object(
            self.queryset,
            pk
        )
        if not player:
            return self.get_json_response('No such player', 'error')

        serializer: PlayerSerializer = PlayerSerializer(
            player,
            data=request.data,
            partial=True
        )
        if not serializer.is_valid():
            return self.get_json_response(serializer.errors, 'error')
        serializer.save()
        return self.get_json_response('Partially Updated', 'success')

    def destroy(self, request: Request, pk: str) -> Response:
        """DELETE method."""

        player: Optional[Player] = self.get_object(
            self.queryset,
            pk
        )
        if not player:
            return self.get_json_response('No such player', 'error')
        player.delete()
        return self.get_json_response('Player deleted', 'error')