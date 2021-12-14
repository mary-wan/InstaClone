"""InstaClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from instagram import views as insta_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('instagram.urls')),
    path('tinymce /', include('tinymce.urls')),
    path('accounts/register/',insta_views.register, name='register'),
    path('accounts/login/',auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/',include('social_django.urls',namespace='social')),
    # path('password-reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
    #      name='password_reset'),
    # path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    #      name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    #      name='password_reset_confirm'),
    


    
]

