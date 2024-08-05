from rest_framework import permissions

from api_yamdb import constants


class IsAuthorModeratorAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object or
    moderators/admins to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and (obj.author == request.user
                         or request.user.role == constants.MODERATOR
                         or request.user.is_admin)))


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission that's allow edit access to users with the 'admin' role.
    """

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_admin)


class IsAdmin(permissions.BasePermission):
    """
    Admin and superuser permission.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
