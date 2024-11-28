from django.contrib import admin
from .models import User

from authentication.models import Role

# Create roles
Role.objects.get_or_create(name="Manager")
Role.objects.get_or_create(name="Admin")
Role.objects.get_or_create(name="User")
Role.objects.get_or_create(name="Developer")

print("Roles added successfully!")

# Register your models here
admin.site.register(User)
admin.site.register(Role)

