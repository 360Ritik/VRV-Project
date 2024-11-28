from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    """
    Custom permission to check if the user has any of the required roles.
    """

    def has_permission(self, request, view):
        # Get the required roles from the view
        required_roles = getattr(view, 'required_roles', None)

        if required_roles is None:
            # If no roles are specified, allow access
            return True

        # Check if the user has any of the required roles
        user_roles = request.user.roles.values_list('name', flat=True)
        return bool(set(required_roles) & set(user_roles))
