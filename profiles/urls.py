from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.display_user, name='profiles'),

    path('password_change/', views.change_password, name='password_change_index'),
    path(
        'password_change_done/', 
        auth_views.PasswordChangeDoneView.as_view(
            template_name='pages/profiles/password_change_done.html'
        ), 
        name="password_change_done"
    ),
]
