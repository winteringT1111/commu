from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('notice', views.notice, name='notice'),
    path('world', views.world, name='world'),
    path('system', views.system, name='system'),
    path('system/total', views.totalsystem, name='totalsystem'),
    path('attendance/', views.attendance, name='attendance'),
    path('class/potion/', views.potion, name='potion'),
    path('check_combination/', views.check_combination, name='check_combination'),
]