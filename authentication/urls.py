from django.urls import path
from .views import RegisterView, LoginView, RoleProtectedView, AdminAndManager, AdminOnlyView, ManagerOnlyView, ManagerAndDeveloperView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', RoleProtectedView.as_view(), name='admin-view'),
   path('manager-developer/', ManagerAndDeveloperView.as_view(), name='manager-developer-view'),
    path('manager-only/', ManagerOnlyView.as_view(), name='manager-only-view'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only-view'),
    path('admin-manager/', AdminAndManager.as_view(), name='admin-admin-only-view'),
   path('logout/', LogoutView.as_view(), name='logout'),
]
