from django.urls import path, include
from .views import index, Faq

app_name = 'product'


urlpatterns = [
    path('', index, name='index'),
    path('faq/', Faq, name='faq'),
]