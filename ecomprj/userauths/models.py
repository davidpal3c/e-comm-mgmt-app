from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)  # email unique and must NOT be provided always since abstract authentication will be user (google auth)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)

    USERNAME_FIELD = "email"                # so that email can be taken as username
    REQUIRED_FIELDS = ['username']      


    def __str__(self):          
        return self.username
    