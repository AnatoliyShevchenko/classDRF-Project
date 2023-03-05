from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from typing import Any


class TeacherPermission(BasePermission):
    """Avada Kedavra kurva."""

    def has_permission(self, request: Request, view: Any) -> bool:
        student: bool = (
            request.user and request.user.is_student
        )
        teacher: bool = request.user.is_teacher
        if view.action in (
            'list',
        ):
            return student
        
        elif view.action in (
            'list',
            'retrieve',
            'create',
            'update',
            'partial_update',
            'destroy'
        ):
            return teacher