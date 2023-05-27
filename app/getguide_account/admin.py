from django.contrib import admin
# from accounts.forms import MyUserChangeForm, MyUserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django import forms

from .models import *
from django import forms
# from phonenumber_field.widgets import PhoneNumberPrefixWidget

# class ContactForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'phone': PhoneNumberPrefixWidget(),
#         }




User = get_user_model()


admin.site.register(GuideImage)
admin.site.register(BusyDates)
admin.site.register(Language)
admin.site.register(Region)



class ImageInline(admin.StackedInline):
    model = GuideImage
    max_num = 5
    extra = 1




@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name','image','company_name','birthday','phone')}),
        (_('Work Info'), {'fields': (
            'video','id_image' ,'languages','regions',)}),
        (_('Permissions'), {'fields': ('is_active','is_accepted','is_finished','is_guide','is_company','is_driver','is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("first_name", "last_name", 'email', 'password1', 'password2'),
        }),
    )
    # # The forms to add and change user instances
    # form = MyUserChangeForm
    # add_form = MyUserCreationForm
    list_display = ('first_name','last_name','email','is_superuser','is_active','is_finished')
    list_display_links=('first_name','last_name','email')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups','is_guide','is_company','is_driver','is_accepted')
    inlines = [ImageInline,]
    # form = ContactForm
    # search_fields = ('first_name', 'last_name', 'email')
    # ordering = ('-date_joined',)
    # filter_horizontal = ('groups', 'user_permissions',)




