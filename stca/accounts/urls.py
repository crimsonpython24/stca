from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginViewRedirect.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('user_settings/', views.user_settings, name='user_settings'),
    path('test_tmpl_1', views.TemplateTestView.as_view(), name='templatetest'),
    path('test_tmpl_2', views.TemplateTestView2.as_view(), name='templatetest2')
]