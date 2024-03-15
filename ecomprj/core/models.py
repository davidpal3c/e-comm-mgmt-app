from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User


# from sys import prefix
# from pyexpat import model
# from enum import unique
# from pyparsing import alphas


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):

    cid = models.UUIDField(unique=True, length=10, max_length=30, prefix="biscuit", alphabet="abcdefgh12345")  # Custom item id
    title = models.CharField(unique=False, max_length=100)      # Title, Heading
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "Categories"      #

    
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))       # whatever image is uploaded (to the imgage model) would be appended here
    

    def __str__(self):              # defines string representation of objects in database/admin 
        return self.title
    