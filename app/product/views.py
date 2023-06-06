from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import *

user = get_user_model()


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin/')
        # if request.user.is_finished:
        #     if not request.user.is_accepted:
        #         return redirect('account:finish_success')
        #     # return redirect('product:index')
        # else:
        #     return redirect('account:finish_1')
    context = {}

    guides = user.objects.filter(is_guide=True)
    blogs = Blog.objects.all()

    context["guides"] = guides
    context['blogs'] = blogs
    return render(request, 'index.html',context)

def Faq(request):

    return render(request, 'faq.html')


def About(request):

    return render(request,"about.html")


def BlogView(request):
    context={}

    blogs = Blog.objects.all()

    context["blogs"] = blogs

    return render(request,"blogs.html",context)


def SearchResults(request):

    return render(request,"searchResults.html")



