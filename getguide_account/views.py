from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string, get_template
from django.template import Context
from getguide_account.tokens import account_activation_token
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.contrib import messages
from django.utils import timezone
from django.core.mail import EmailMessage


def activation_sent(request):
    return render(request, "activation_sent.html")



def register(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('product:index')

    if request.method == 'POST' and 'btn_guide'in request.POST:
        form_guide = GuideRegisterForm(request.POST, request.FILES or None)
        if form_guide.is_valid():
            user = form_guide.save(commit=False)
            user.is_active = False
            user.is_guide = True
            user.created_date = timezone.now()
            user.save()
            current_site = get_current_site(request)
            print(current_site)
            mail_subject = 'Hesab aktivləşdirilməsi'
            ctx = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }
            message = get_template('account_activate.html').render(ctx)
            to_email = form_guide.cleaned_data.get('email')
            to_list = [to_email]
            from_mail = settings.EMAIL_HOST_USER
            msg = EmailMessage(mail_subject, message, from_mail, to_list)
            msg.content_subtype = 'html'
            msg.send()
            messages.success(request,
                             'Təbriklər,uğurla qeydiyyatdan keçdiniz!Xahiş edirik mailinizə gələn mesajı təsdiq edəsiniz!')
            # return HttpResponseRedirect('/login/')
            return redirect('account:activation_sent')
    else:
        form_guide = GuideRegisterForm()




    if request.method == 'POST' and 'btn_company'in request.POST:
        form_company = CompanyRegisterForm(request.POST, request.FILES or None)

        if form_company.is_valid():
            user = form_company.save(commit=False)

            user.is_active = False
            user.is_company = True
            user.created_date = timezone.now()
            user.save()
            current_site = get_current_site(request)
            print(current_site)
            mail_subject = 'Hesab aktivləşdirilməsi'
            message = render_to_string('account_activate.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            message.content_subtype = 'html'
            to_email = form_company.cleaned_data.get('email')
            to_list = [to_email]
            from_mail = settings.EMAIL_HOST_USER
            send_mail(mail_subject, message, from_mail, to_list)
            messages.success(request,
                             'Təbriklər,uğurla qeydiyyatdan keçdiniz!Xahiş edirik mailinizə gələn mesajı təsdiq edəsiniz!')
            # return HttpResponseRedirect('/login/')
            return redirect('account:activation_sent')



    else:
        form_company = CompanyRegisterForm()

    context['form_company'] = form_company
    context['form_guide'] = form_guide
    return render(request, 'signup.html', context)


def activated_view(request):
    return render(request,"activated.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('products:index')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.<a href="/login">Daxil ol</a>')
        return redirect("account:activated")
    else:
        return HttpResponse('Activation link is invalid!')





def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('product:index')
    next = request.GET.get("next", None)
    if request.method == 'POST' and 'btn_guide' in request.POST:
        form_guide = GuideLoginForm(request.POST or None)
        if form_guide.is_valid():
            email = form_guide.cleaned_data.get('email')
            password = form_guide.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            if next:
                return redirect(next)
        # return redirect('product:index')
    else:
        form_guide = GuideLoginForm()

    if request.method == 'POST' and 'btn_company' in request.POST:
        form_company = CompanyLoginForm(request.POST or None)
        if form_company.is_valid():
            email = form_company.cleaned_data.get('email')
            password = form_company.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            if next:
                return redirect(next)
        # return redirect('product:index')

    else:
        form_company = CompanyLoginForm()


    context['form_guide'] = form_guide
    context['form_company'] = form_company
    return render(request, 'login.html', context)

# def logout_view(request):
#     logout(request)
#     return redirect('product:index')
