from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
