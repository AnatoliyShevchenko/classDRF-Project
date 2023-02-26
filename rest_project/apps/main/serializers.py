from rest_framework import serializers

from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    """PlayerSerializer."""
    
    id = serializers.IntegerField()
    name = serializers.CharField()
    surname = serializers.CharField()
    power = serializers.IntegerField()
    age = serializers.IntegerField()
    status = serializers.SerializerMethodField(
        method_name='get_status'
    )

    class Meta:
        model = Player
        fields = (
            'id',
            'name',
            'surname',
            'power',
            'age',
            'status',
            'fullname'
        )
    
    def get_status(self, obj: Player):
        return f'{obj.status} | {obj.get_status_display()}'

    def get_notes(self, obj: Player) -> list[str]:
        notes: list[str] = []
        if obj.power > 80:
            notes.append('Strong')
        elif obj.power < 60:
            notes.append('Weak')
        else:
            notes.append('Middle')
        return notes


class PlayerDetailSerializer(serializers.ModelSerializer):
    """PlayerSerializer."""
    
    id = serializers.IntegerField()
    name = serializers.CharField()
    surname = serializers.CharField()
    fullname = serializers.CharField()
    power = serializers.IntegerField()
    status = serializers.SerializerMethodField(
        method_name='get_status'
    )

    class Meta:
        model = Player
        fields = (
            'id',
            'name',
            'surname',
            'fullname',
            'power',
            'age',
            'status'
        )
    
    def get_status(self, obj: Player):
        return f"{obj.status} | {obj.get_status_display()}"


class PlayerCreateSerializer(serializers.ModelSerializer):
    """Player Create Serializer."""

    name = serializers.CharField()
    surname = serializers.CharField()
    power = serializers.IntegerField()
    age = serializers.IntegerField()

    class Meta:
        model = Player
        fields = (
            'name',
            'surname',
            'power',
            'age',
            'fullname'
        )
    
    def create(self, validated_data):
        player: Player = Player.objects.create(
            **validated_data
        )
        return player