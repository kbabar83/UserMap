from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(username=self.normalize_email(username))
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        user = self.create_user(password=password, username=username)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
    )
    username = models.CharField(
        max_length=191,
        unique=True
    )
    

    address = models.TextField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{self.username})"

# class User(AbstractUser):
#     address = models.TextField(null=True, blank=True)
#     location = models.PointFielFalsed(null=True, blank=True)
#     phone_number = models.CharField(max_length=20, blank=True)

#     def __str__(self):
#         return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username