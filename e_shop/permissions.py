from rest_framework.permissions import BasePermission


class ActiveEmployeeOnly(BasePermission):
    message = "Только активные сотрудники имеют доступ."

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active)
