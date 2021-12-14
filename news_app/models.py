from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.
class NewsPortal(models.Model):
    title = models.CharField(max_length=100)
    image_link = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    main_content = models.TextField()


    def __str__(self):
        return self.title