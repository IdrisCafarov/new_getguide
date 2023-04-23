from django.urls import path,re_path
from .views import *

app_name = 'account'


urlpatterns = [
    path('signup/',register, name='register'),
    path('login/', login_view, name="login"),
    path('sent/',activation_sent, name="activation_sent"),
    path('logout/',logout_view,name='logout'),
    path('activated/',activated_view, name="activated"),
    path('finish_1',first_finish_view, name="finish_1"),
    path('finish_2',second_finish_view, name="finish_2"),
    path('finish_3',third_finish_view, name="finish_3"),
    path('finish_sucess',finish_success, name="finish_success"),
    path('myProfile', my_profile, name='my_profile'),
    path('forgot_password',forgot_password,name="forgot_password"),
    path("add_busy_date/", BusyDateView.as_view({'post': 'create',}), name="add_busy_date"),
    path("show_busy_date/", UserBusyDateView.as_view({'get': 'list',}), name="show_busy_date"),
    path("show_busy_date/<pk>/", UserBusyDateView.as_view({'get': 'retrieve',}), name="show_busy_date_detail"),



    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        activate, name='activate'),
]