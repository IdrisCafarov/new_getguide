from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from django.conf import settings
from django.core import validators
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import EmailMessage
# from django.contrib.auth import get_user_model

# User = get_user_model()
# from product.helper import seo
# from accounts.options import USERTYPE
# from phone_field import PhoneField

from django.db import models
from django.db.models import signals
from django.db.models.signals import pre_save
from django.dispatch import receiver



USER_MODEL = settings.AUTH_USER_MODEL


class Language(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name





class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), null=True, max_length=100, unique=False)
    first_name = models.CharField(_('first name'), max_length=255, blank=True, )
    company_name = models.CharField(_('company name'), max_length=50, blank=True)
    phone = models.CharField(_("phone number"), blank=True, null=True, max_length=15)
    birthday = models.DateField(_("birth date"), blank=True, null=True)
    # usertype = models.IntegerField(verbose_name="Cins",choices=USERTYPE,null=True,blank=True,default=1)

    languages = models.ManyToManyField(Language,null=True,blank=True)

    regions = models.ManyToManyField(Region,null=True,blank=True)


    image = models.FileField(_("image"),null=True,blank=True,upload_to="user_pp")

    id_image = models.ImageField(_("Id image"), null=True,blank=True,upload_to="user_id")

    video = models.FileField(_("video"),null=True,blank=True,upload_to="user_video")

    last_name = models.CharField(_('last name'), max_length=255, blank=True)
    # image=models.ImageField(_('Add Photo'),null=True)

    email = models.EmailField(_('email address'), unique=True, max_length=255, blank=False)

    slug = models.SlugField(unique=True, editable=False, null=True)

    # is_customer = models.BooleanField(_('user customer'), default=False)

    is_guide = models.BooleanField(_('user guide'), default=False)

    is_company = models.BooleanField(_('user company'), default=False)

    is_driver = models.BooleanField(_('user driver'), default=False)

    is_finished = models.BooleanField(_('account filling finished'), default=False)

    is_accepted = models.BooleanField(_('User accepted'), default=False)






    # is_pro = models.BooleanField(_('pro seller'), default=False)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()




    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        managed = True


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.languages:
    #         self.languages= eval(self.languages)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        super(MyUser, self).save(*args, **kwargs)
        # self.slug = "{}.{}".format(seo(self.first_name + "-" + self.last_name), self.id)
        # super(MyUser, self).save(*args, **kwargs)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()

    def get_avatar(self):
        if self.image:
            return self.image.url
        else:
            return "/static/images/user_pp.png"


    # @receiver(signals.post_save, sender=self)
    # def create_product(self, sender, instance, created, **kwargs):
    #     if self.


@receiver(pre_save, sender=MyUser)
def on_change(sender, instance: MyUser, **kwargs):
    if instance.id is None: # new object will be created
        pass # write your code here
    else:
        previous = MyUser.objects.get(id=instance.id)
        if previous.is_accepted != instance.is_accepted: # field will be updated

            if previous.is_accepted == False:
                 email = EmailMessage(
                     subject="Account Status",
                     body="Your account activated ",
                     from_email=settings.EMAIL_HOST_USER,
                     to=[instance.email,]
                     )
            else:
                email = EmailMessage(
                     subject="Account Status",
                     body="Your account suspended ",
                     from_email=settings.EMAIL_HOST_USER,
                     to=[instance.email,]
                     )

            email.send()

class GuideImage(models.Model):
    image = models.ImageField(upload_to="Guide Images")
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name="images")


class BusyDates(models.Model):
    date = models.DateField()
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name="busy_dates")