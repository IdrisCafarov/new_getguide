from django.urls import path, include
from .views import *

app_name = 'product'


urlpatterns = [
    path('', index, name='index'),
    path('faq/', Faq, name='faq'),
    path('about/',About,name="about"),
    path('blogs',BlogView,name="blogs")
    # path('blog_detail/<id>/')
]