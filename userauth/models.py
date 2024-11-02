from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from userauth.manager import UserManager #import from account apps



class UserAuth(AbstractBaseUser,PermissionsMixin):
    class Meta:
        verbose_name_plural = "User"
    profile_pic = models.ImageField(upload_to='faces/', default='faces/profile.png')
    username = models.CharField(max_length=10,unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=14)
    sponsor_id = models.CharField(max_length=14)
    rating_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = UserManager()

    def __str__(self):
        return self.username