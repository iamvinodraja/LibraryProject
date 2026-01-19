"""
Custom permission classes for library API.
"""
from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to edit.
    Read-only access for unauthenticated users.
    """
    def has_permission(self, request, view):
        # Read permissions (GET, HEAD, OPTIONS) for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for authenticated users
        return request.user and request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only for the owner
        # This assumes the model has a 'user' or 'owner' field
        return obj.user == request.user if hasattr(obj, 'user') else True


class IsBorrowerOrAdmin(permissions.BasePermission):
    """
    Custom permission for borrow records.
    Only the member who borrowed or admin can view/modify.
    """
    def has_object_permission(self, request, view, obj):
        # Admins can do anything
        if request.user and request.user.is_staff:
            return True
        
        # For borrow records, check if user is the borrower
        if hasattr(obj, 'member'):
            # Check if the logged-in user is associated with the member
            return request.user.is_authenticated
        
        return False