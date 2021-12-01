from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from ecom_app.views import users_views as views

urlpatterns = [
    path('register-admin/', views.register_admin_user,
         name='users-register-admin'),
    path('register/', views.register_user, name='users-register'),
    path('login/', TokenObtainPairView.as_view(), name='users-login'),
    path('profile/', views.get_user_profile, name="users-profile"),
]
