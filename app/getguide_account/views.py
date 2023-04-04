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
from email.mime.image import MIMEImage
import os


def activation_sent(request):

    return render(request, "signup/activation_sent.html")



def register(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('product:index')

    if request.method == 'POST':
        check_guide = request.POST.get("guide")
        check_company = request.POST.get("company")
        check_driver = request.POST.get("driver")
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            if check_guide=="on":
                user.is_guide=True
            elif check_company=="on":
                user.is_company=True
            elif check_driver=="on":
                user.is_driver=True

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
            message = get_template('signup/account_activate.html').render(ctx)
            to_email = form.cleaned_data.get('email')
            to_list = [to_email]
            from_mail = settings.EMAIL_HOST_USER
            msg = EmailMessage(mail_subject, message, from_mail, to_list)
            msg.content_subtype = 'html'
            msg.mixed_subtype = 'related'
            # msg.attach_alternative(body_html, "text/html")
            img_dir = 'static/images'
            image = 'Logo.png'
            file_path = os.path.join(img_dir, image)
            with open(file_path, 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-ID', '<{name}>'.format(name=image))
                img.add_header('Content-Disposition', 'inline', filename=image)
            msg.attach(img)
            msg.send()
            # messages.success(request,
            #                  'Təbriklər,uğurla qeydiyyatdan keçdiniz!Xahiş edirik mailinizə gələn mesajı təsdiq edəsiniz!')
            # return HttpResponseRedirect('/login/')
            return redirect('account:activation_sent')
    else:
        form = RegisterForm()







    context['form'] = form
    return render(request, 'signup/signup.html', context)


def activated_view(request):
    return render(request,"signup/activated.html")


def activate(request, uidb64, token):
    if request.user.is_authenticated:
        logout(request)
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
        if request.user.is_finished:
            if not request.user.is_accepted:
                return redirect('account:finish_success')
            return redirect('product:index')
        return redirect('account:finish_1')
    next = request.GET.get("next", None)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('product:index')

        else:
            messages.error(request,'Email ve ya Parol yanlisdir!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        form = LoginForm()




    context['form'] = form

    return render(request, 'login/login.html', context)




def logout_view(request):
    logout(request)
    return redirect('account:login')



def first_finish_view(request):
    if not request.user.is_authenticated:
        return redirect('product:index')
    elif request.user.is_finished:
        if not request.user.is_accepted:
            return redirect('account:finish_success')
        return redirect('product:index')


    return render(request,"activation_after_login/finish_1.html")


def second_finish_view(request):

    if not request.user.is_authenticated:
        return redirect('product:index')
    elif request.user.is_finished:
        if not request.user.is_accepted:
            return redirect('account:finish_success')
        return redirect('product:index')


    context = {}

    usr = get_object_or_404(MyUser, id=request.user.id)
    if request.method == 'POST':
        print("amma burda yoxam")
        form = FirstVerificationForm(request.POST, request.FILES or None, instance=usr)
        if form.is_valid():
            print("burda hec yoxam")
            user = form.save(commit=False)
            # user.is_finished = True
            user.save()
            return redirect('account:finish_3')
    else:
        form = FirstVerificationForm()







    context['form'] = form
    return render(request,"activation_after_login/finish_2.html",context)


def third_finish_view(request):

    if not request.user.is_authenticated:
        return redirect('product:index')
    elif request.user.is_finished:
        if not request.user.is_accepted:
            return redirect('account:finish_success')
        return redirect('product:index')


    context = {}
    # if not request.user.is_authenticated:
    #     return redirect('product:index')
    usr = get_object_or_404(MyUser, id=request.user.id)
    if request.method == 'POST':
        print("qaqa buradayam")
        form = SecondVerificationForm(request.POST, request.FILES or None, instance=usr)
        print(form)
        if form.is_valid():
            print("indi de burda")
            user = form.save(commit=False)
            user.is_finished = True
            user.save()
            return redirect('account:finish_success')
    else:
        form = SecondVerificationForm()







    context['form'] = form
    return render(request,"activation_after_login/finish_3.html",context)



def finish_success(request):
    if not request.user.is_authenticated:
        return redirect('product:index')
    # elif  request.user.is_finished:
    #     return redirect('product:index')
    return render(request,"activation_after_login/finish_success.html")




def my_profile(request):
    context = {}
    if request.user.is_authenticated:
        if request.user.is_finished:
            if not request.user.is_accepted:
                return redirect('account:finish_success')
            # return redirect('product:index')
        else:
            return redirect('account:finish_1')

    usr = get_object_or_404(MyUser, id=request.user.id)
    if request.method == 'POST':
        form = UpdatePersonalForm(request.POST, request.FILES or None, instance=usr)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_finished = True
            user.save()
            messages.success(request,
                             'Təbriklər,uğurla update etdiniz!')
            return redirect('account:my_profile')
    else:
        form = UpdatePersonalForm(instance=usr)


    context["form"] = form
    return render(request,"myProfile.html",context)



def forgot_password(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            return HttpResponse("Yay! you are human.")
        else:
            return HttpResponse("OOPS! Bot suspected.")

    else:
        form = ContactForm()

    return render(request, 'login/forgot_password.html', {'form':form})
