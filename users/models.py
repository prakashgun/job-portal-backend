from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class State(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Advertiser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
