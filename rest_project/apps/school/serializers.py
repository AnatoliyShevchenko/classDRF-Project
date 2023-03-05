from rest_framework import serializers

from auths.models import Client


class StudentsSerializer(serializers.ModelSerializer):
    """Serializer for list students."""

    class Meta:
        model = Client
        fields = (
            'id',
            'email',
            'is_student',
            'date_joined'
        )


class TeacherSerializer(serializers.ModelSerializer):
    """Serializer for list teacher."""

    class Meta:
        model = Client
        fields = (
            'id',
            'email',
            'is_teacher',
            'date_joined'
        )