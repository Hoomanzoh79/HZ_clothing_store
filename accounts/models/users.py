from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_staff = models.BooleanField(default=False,null=True)
    is_superuser = models.BooleanField(default=False,null=True)
    is_active = models.BooleanField(default=True,null=True)
