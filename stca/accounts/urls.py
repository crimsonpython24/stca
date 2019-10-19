from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginViewRedirect.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('user_settings', views.SettingsView.as_view(), name="user_settings"),
    path('user_settings/name', views.user_settings_name, name='user_settings_name'),
    path('user_settings/text', views.user_settings_text, name='user_settings_text'),
    path('user_settings/avatar', views.user_settings_avatar, name='user_settings_avatar'),
]