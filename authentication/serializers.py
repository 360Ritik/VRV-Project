from rest_framework import serializers

from .models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'roles']


class RegisterSerializer(serializers.ModelSerializer):
    roles = serializers.ListField(child=serializers.CharField(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'roles']

    def create(self, validated_data):
        roles_data = validated_data.pop('roles', [])
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        if roles_data:
            roles = Role.objects.filter(name__in=roles_data)
            user.roles.set(roles)  # This handles the insertion in the join table automatically

        user.save()
        return user

