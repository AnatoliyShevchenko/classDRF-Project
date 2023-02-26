# DRF
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
# Django
from django.db.models import QuerySet
# Local
from .models import Player
from .mixins import SomeMixin
from .serializers import (
    PlayerSerializer, 
    PlayerDetailSerializer,
)
# Python
from typing import Optional


class MainView(ViewSet, SomeMixin):
    """MainView."""

    queryset = Player.objects.all()

    def list(self, request: Request) -> Response:
        """GET Method. get all objects."""
        players: QuerySet[Player] = self.queryset.all()
        serializer: PlayerSerializer = \
        PlayerSerializer(
            players,
            many=True
        )
        return Response(
            {
                'Players': serializer.data
            }
        )

    def retrieve(self, request: Request, pk: str) -> Response:
        """GET Method. get some object."""

        player: Optional[Player] = None
        player: Optional[Player] = \
            self.get_and_return_player(
                int(pk)
            )
        if not player:
            return Response('error')

        return Response('success')

    def create(self, request: Request) -> Response:
        data = self.create_object(request)
        if data:
            return Response({
                'data' : 'success'
            })
        return Response({
            'error' : 'error'
        })

    def update(self, request: Request, pk: str) -> Response:
        player = Player.objects.get(id=pk)
        try:
            player = self.queryset.get(
                id=pk
            )
            serializer: PlayerDetailSerializer = \
            PlayerDetailSerializer(player)
        except Player.DoesNotExist:
            return Response({
                'message': 'error'
            })
        else:
            serializer = PlayerSerializer(player, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message" : "ok"
                })
            return Response({
                "error" : serializer.errors
            })

    def partial_update(self, request: Request, pk: str) -> Response:
        player = Player.objects.get(id=pk)
        try:
            player = self.queryset.get(
                id=pk
            )
            serializer: PlayerDetailSerializer = \
            PlayerDetailSerializer(player)
        except Player.DoesNotExist:
            return Response({
                'message': 'error'
            })
        else:
            serializer = PlayerSerializer(
                player, 
                data=request.data, 
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message" : "ok"
                })
            return Response({
                "error" : serializer.errors
            })

    def destroy(self, request: Request, pk: str) -> Response:
        player = Player.objects.get(id=pk)
        try:
            player = self.queryset.get(id=pk)
            player.delete()
            return Response({
                'message' : "ok"
            })
        except Player.DoesNotExist:
            return Response({
                'error': 'Player Does Not Exist'
            })