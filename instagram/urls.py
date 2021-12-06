from django.urls import path
from django.conf.urls import url
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('profile/<username>/', views.profile, name='profile'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('like/<id>', views.like, name='like'),
    path('post/<id>', views.comment, name='comment'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    url(r'^ search/',views.search, name='search'),
]
