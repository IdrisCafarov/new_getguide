from django.urls import path, include
from .views import *

app_name = 'product'


urlpatterns = [
    path('', index, name='index'),
    path('faq/', Faq, name='faq'),
    path('about/',About,name="about"),
    path('blogs',BlogView,name="blogs"),
    path('search_results',SearchResults,name="search_results")
    # path('blog_detail/<id>/')
]