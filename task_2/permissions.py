from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profiles"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnCourse(permissions.BasePermission):
    """Allow instructors to update their own courses only"""

    def has_object_permission(self, request, view, obj):
        """Check the instructor is trying to update their own course"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.instructor.id == request.user.id

class UpdateOwnArticle(permissions.BasePermission):
    """Allow authors to update their own articles only"""

    def has_object_permission(self, request, view, obj):
        """Check the author is trying to update their own article"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author.id == request.user.id
