from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('', views.login, name='users_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.signup, name='users_signup'),
]   