from django.db import models
from .helper import seo
from django.urls import reverse






class GeneralSettings(models.Model):
    logo = models.ImageField(upload_to="General Images")

class Blog(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Products')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)
        self.slug = seo(self.name + "-" + str(self.id))
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})







