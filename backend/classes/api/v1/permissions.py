from rest_framework import permissions


class HasClassPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ["create", "update", "partial_update"]:
            return request.user.is_teacher or request.user.is_school
        elif view.action == "destroy":
            return request.user.is_school

        return True


class HasClassVideoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ["create", "update", "partial_update"]:
            return request.user.is_teacher or request.user.is_school
        elif view.action == "destroy":
            return request.user.is_teacher or request.user.is_school

        return True


class HasClassVideoCommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ["create", "update", "partial_update", "destroy"]:
            return request.user.is_teacher

        return True
