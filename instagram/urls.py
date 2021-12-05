from django.urls import path
from django.conf.urls import url
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    # url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    # re_path(r"^post/(\d+)", views.comment, name="comment"),
    url(r"^like/(\d+)", views.like, name="like"),
    # url(r"^post/(\d+)", views.post_comment, name="comment"),
    path('post/<id>', views.comment, name='comment'),
    path('profile/',views.profile, name='profile'),
]
