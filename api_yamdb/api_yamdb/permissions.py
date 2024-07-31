from rest_framework import permissions


class IsAuthorModeratorAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object or
    moderators/admins to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return (obj.author == request.user or
                    request.user.role == 'moderator' or
                    request.user.role == 'admin')


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow access to users with the 'admin' role.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.role == 'admin')
