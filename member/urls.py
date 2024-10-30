from django.urls import path
from member import views

app_name = 'member'

urlpatterns = [
    path('member', views.member_main, name='member_main'),
    path('member/<str:username>', views.member_profile, name='member_profile'),
    path('giftbox', views.giftbox, name='giftbox'),
]