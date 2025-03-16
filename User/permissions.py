from rest_framework.permissions import BasePermission

class IsUnion(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm("User.is_union"))