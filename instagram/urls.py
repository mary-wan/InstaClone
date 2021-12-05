from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    # url(r"^comment/(\d+)", views.comment, name="comment"),
    url(r"^like/(\d+)", views.like, name="like"),
    url(r"^post/(\d+)", views.post, name="post"),
    path('profile/',views.profile, name='profile'),
]
