
from .models import User
from .serializers import RegisterSerializer
from authentication.permissions import RolePermission
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class RoleProtectedView(APIView):
    permission_classes = [RolePermission]
    required_roles = ['User']

    def get(self, request):
        return Response({"message": "Hello, you have access as user!"})


class ManagerAndDeveloperView(APIView):
    permission_classes = [RolePermission]
    required_roles = ['Manager', 'Developer']  # Define required roles here

    def get(self, request):
        return Response({"message": "Hello, you have access as Manager or Developer!"})


class ManagerOnlyView(APIView):
    permission_classes = [RolePermission]
    required_roles = ['Manager']  # Only Manager role required

    def get(self, request):
        return Response({"message": "Hello, you have access as Manager!"})


class AdminOnlyView(APIView):
    permission_classes = [RolePermission]
    required_roles = ['Admin']  # Only Admin role required

    def get(self, request):
        return Response({"message": "Hello, you have access as Admin!"})


class AdminAndManager(APIView):
    permission_classes = [RolePermission]
    required_roles = ['Admin', 'Manager']  # Redundant but added to meet the requirement

    def get(self, request):
        return Response({"message": "Hello, you have access as Admin or Manager!"})


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            # Get the refresh token from the request header
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({"error": "No refresh token provided"}, status=status.HTTP_400_BAD_REQUEST)

            # Create a RefreshToken object from the refresh token string
            token = RefreshToken(refresh_token)

            # Blacklist the token
            token.blacklist()

            return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)