from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import *

user = get_user_model()


# Create your views here.

def index(request):
    context = {}

    guides = user.objects.filter(is_guide=True)
    blogs = Blogs.objects.all()

    context["guides"] = guides
    context['blogs'] = blogs
    return render(request, 'index.html',context)

def Faq(request):

    return render(request, 'faq.html')