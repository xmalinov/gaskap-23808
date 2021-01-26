from rest_framework import permissions


class HasNewsPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ["create", "update", "partial_update"]:
            return request.user.is_teacher or request.user.is_school
        elif view.action == "destroy":
            return request.user.is_school

        return True


class HasNewsCommentPermissions(permissions.BasePermission):
    def has_permisison(self, request, view):
        if view.action in ["create", "update", "partial_update"]:
            return request.user.is_teacher or request.user.is_school
        elif view.action == "destroy":
            return request.user.is_teacher

        return True
