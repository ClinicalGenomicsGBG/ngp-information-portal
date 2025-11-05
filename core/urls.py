"""
URL configuration for portal_template project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", include("home.urls")),
    
    # Session update URL
    path("update_session/", views.update_session, name="update_session"),

    # Account related URLs
    path("profiles/", include("profiles.urls"), name="profiles"),

    path('accounts/password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path(
        'accounts/password_reset_confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), 
        name='password_reset_confirm'
    ),
    path(
        'accounts/password_reset_done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ), 
        name='password_reset_done'
    ),
    path(
        'accounts/password_reset_complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ), 
        name='password_reset_complete'
    ),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path("admin/", admin.site.urls),
]
