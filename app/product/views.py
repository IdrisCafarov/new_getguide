from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import *

user = get_user_model()


# Create your views here.

def index(request):
    # if request.user.is_authenticated:
    #     if request.user.is_finished:
    #         if not request.user.is_accepted:
    #             return redirect('account:finish_success')
    #         # return redirect('product:index')
    #     else:
    #         return redirect('account:finish_1')
    context = {}

    guides = user.objects.filter(is_guide=True)
    blogs = Blog.objects.all()

    context["guides"] = guides
    context['blogs'] = blogs
    return render(request, 'index.html',context)

def Faq(request):

    return render(request, 'faq.html')



