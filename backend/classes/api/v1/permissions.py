from rest_framework import permissions


class HasClassPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        actions = ["create", "update", "partial_update"]
        if view.action in actions:
            return request.user.is_teacher or request.user.is_school
        elif view.action == "destroy":
            return request.user.is_school

        return True
