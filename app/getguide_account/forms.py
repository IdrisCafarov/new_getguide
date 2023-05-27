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
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.formfields import PhoneNumberField
# from PIL import Image
# from user.models import *

# get custom user
User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'type':'text',
        'id':'signUpEmail',
        'placeholder':'Enter your email',
        }
    ))

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
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = MyUser.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Bu email artıq mövcuddur.Yenisini yoxlayın!')



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""



class LoginForm(forms.Form):
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



        return super(LoginForm, self).clean()



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class FirstVerificationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Enter your Name',
        }
    ))

    last_name = forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
        'type':'text',
        'placeholder':'Enter your Last Name',

        }
    ))
    id_image = forms.ImageField(max_length=100,widget=forms.FileInput(
        attrs={
        'class':'hiden',
        'type':'file',
        'id':'file',
        'name':'img',
        'accept':'image/*'
        }
    ))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'id_image')




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""







class SecondVerificationForm(forms.ModelForm):



    languages = forms.ModelMultipleChoiceField(queryset=Language.objects.all(),widget=forms.SelectMultiple(attrs={
        'class':'langSelect',
        'name':'languages',
        'id':'languages',
        'multiple': True
        }
    ))

    regions = forms.ModelMultipleChoiceField(queryset=Region.objects.all(),widget=forms.SelectMultiple(attrs={
        'class':'langSelect',
        'name':'regions',
        'id':'regions',
        'multiple': True
        }
    ))


    phone = PhoneNumberField(max_length=100,widget=PhoneNumberPrefixWidget(
        attrs={
        'type':'text',
        'placeholder':'Enter your Last Name',

        }
    ))



    class Meta:

        model = User
        fields = ('languages','regions','phone')





    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
        # if self.languages:
        #     self.languages= eval(self.languages)

    def clean_languages(self):
        data = self.cleaned_data.get('languages')
        if data == self.fields['languages'].choices[0][0]:
            raise forms.ValidationError('This field is required')
        return data



class UpdatePersonalForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Enter your Name',
        }
    ))

    last_name = forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
        'type':'text',
        'placeholder':'Enter your Last Name',

        }
    ))

    email = forms.EmailField(max_length=100,widget=forms.EmailInput(
        attrs={
        'type':'text',
        'placeholder':'Enter your Email',
        'readonly':True

        }
    ))

    phone = forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
        'type':'text',
        'placeholder':'Enter your Last Name',
        'readonly':True

        }
    ))
    # image = forms.ImageField(max_length=100,widget=forms.FileInput(
    #     attrs={
    #     'class':'hiden',
    #     'type':'file',
    #     'id':'file',
    #     'name':'img',
    #     'accept':'image/*'
    #     }
    # ))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','phone')




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""





############ Test ############
class ContactForm(forms.Form):

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""