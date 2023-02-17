from django.urls import path,re_path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'account'


urlpatterns = [
    path('signup/',register, name='register'),
    path('login/', login_view, name="login"),
    path('sent/',activation_sent, name="activation_sent"),
    path('activated/',activated_view, name="activated"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        activate, name='activate'),
]