from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from getguide_account.models import *
# from PIL import Image
# from user.models import *

# get custom user
User = get_user_model()

class GuideRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'type':'text',
        'id':'signUpEmail',
        'placeholder':'Enter your email',
        }
    ))
    first_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
        'type':'text',
        'id':'signUpNamel',
        'placeholder':'Enter your name',
        'autofocus': True,
        }))
    last_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
        'type':'text',
        'id':'signUpNamel',
        'placeholder':'Enter your surname',
        }))
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(
        attrs={
        'type':'password',
        'id':'signUpPass',
        'placeholder':'Enter your password',

        }
    ))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(
        attrs={
        'type':'password',
        'id':'signUpPass',
        'placeholder':'Enter your password',
        }
    ))


    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = MyUser.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Bu email artıq mövcuddur.Yenisini yoxlayın!')
    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            match = MyUser.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Bu istifadəçi adı artıq mövcuddur.Yenisini yoxlayın!')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

class CompanyRegisterForm(UserCreationForm):

    company_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
        'type':'text',
        'id':'name',
        'placeholder':'Enter Company name',
        'autofocus': True,
        }))

    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'type':'text',
        'id':'email',
        'placeholder':'Enter Company email',
        }
    ))

    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(
        attrs={
        'type':'password',
        'id':'password',
        'placeholder':'Enter password',
        }
    ))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(
        attrs={
        'type':'password',
        'id':'password',
        'placeholder':'Enter password again',
        }
    ))


    class Meta:
        model = User
        fields = ('company_name','email')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = MyUser.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Bu email artıq mövcuddur.Yenisini yoxlayın!')
    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            match = MyUser.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Bu istifadəçi adı artıq mövcuddur.Yenisini yoxlayın!')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""



class GuideLoginForm(forms.Form):
    email= forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'type':'text',
        'id':'loginEmail',
        'placeholder':'Enter your Email'
        }
    ))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        'type':'password',
        'id':'loginPass',
        'placeholder':'Enter your Password'
        }
    ))

    def clean(self):
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        if email and password:
            user=authenticate(email=email,password=password)
            if not user:
                raise forms.ValidationError('Email or Password is incorrect')

            elif not user.is_guide:
                raise forms.ValidationError('Email or Password is incorrect')


        return super(GuideLoginForm, self).clean()



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class CompanyLoginForm(forms.Form):
    email= forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'type':'text',
        'id':'loginEmail',
        'placeholder':'Enter your Email'
        }
    ))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        'type':'password',
        'id':'loginPass',
        'placeholder':'Enter your Password'
        }
    ))

    def clean(self):
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        if email and password:
            user=authenticate(email=email,password=password)
            if not user:
                raise forms.ValidationError('Email or Password is incorrect')

            elif not user.is_company:
                raise forms.ValidationError('Email or Password is incorrect')


        return super(CompanyLoginForm, self).clean()



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""