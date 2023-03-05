from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny

from django.db.models.query import QuerySet

from auths.models import Client
from .serializers import StudentsSerializer, TeacherSerializer
from abstracts.mixins import ResponseMixin, ObjectMixin
from .permissions import TeacherPermission

from typing import Optional


class StudentsViewSet(ViewSet, ResponseMixin, ObjectMixin):
    """ViewSet for students."""

    permission_classes = (
        TeacherPermission, 
        # AllowAny,
    )
    queryset: QuerySet = Client.objects.filter(
        is_student=True,
    )

    def list(self, request: Request) -> Response:
        students: QuerySet[Client] = self.queryset.all()
        serializer: StudentsSerializer =\
            StudentsSerializer(
                students,
                many=True
            )
        return self.get_json_response(serializer.data, 'success')
    
    def retrieve(self, request: Request, pk: str) -> Response:
        student: Optional[Client] = self.get_object(
            self.queryset,
            pk
        )
        if not student:
            return self.get_json_response('No such student', 'error')
        return self.get_json_response(
            {
                'email': student.email,
                'date_joined': student.date_joined,
                'is_student': student.is_student
            }
        )
    

class TeacherViewSet(ViewSet, ResponseMixin, ObjectMixin):
    """ViewSet for teacher."""

    permission_classes = (AllowAny,)
    queryset: QuerySet = Client.objects.filter(is_teacher=True)

    def list(self, request: Request) -> Response:
        teachers: QuerySet[Client] = self.queryset.all()
        serializer: TeacherSerializer =\
            TeacherSerializer(
                teachers,
                many=True
            )
        return self.get_json_response(serializer.data, 'success')