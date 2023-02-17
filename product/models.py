from django.db import models
from .helper import seo
from .utils import create_slug_shortcode
# Create your models here.
from django.contrib.auth import get_user_model

user = get_user_model()



# class Guides(models.Model):
#     user = models.ForeignKey(user,on_delete=models.CASCADE,related_name="user")
#     image = models.ImageField(upload_to="Guides")
#     description = models.TextField()
#     price = models.FloatField()


#     def __str__(self):
#         return self.name

class Blogs(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Products')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=Blogs)

        super(Blogs, self).save(*args, **kwargs)

