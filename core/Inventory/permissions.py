from accounts.models import CustomUser
from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'manager'

class IsAdminOrManager(BasePermission):
    """
    Allows access only to users with role 'admin' or 'manager'.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in ['admin', 'manager']
        )
