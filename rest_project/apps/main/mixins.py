from rest_framework.request import Request

from typing import Optional, Any

from .serializers import PlayerCreateSerializer
from .models import Player


class SomeMixin:
    """Mixin for finding object."""

    def get_and_return_player(
        self, 
        obj_id: int
    ) -> Optional[Player]:
        try:
            player = self.queryset.get(
                id=obj_id
            )
        except Player.DoesNotExist:
            return None
        else:
            return player

    def create_object(
        self,
        request: Request
    ) -> Optional[Any]:
        try:
            serializer: PlayerCreateSerializer = \
            PlayerCreateSerializer(data=request.data)
            if serializer.is_valid():
                player: Player = serializer.save()
                return player
        except:
            return serializer.errors