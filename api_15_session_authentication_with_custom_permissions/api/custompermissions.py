from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, views):
        if request.method == "POST":
            return True
        return False
