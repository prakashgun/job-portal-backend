from django.db import models

from users.models import Advertiser


class Vacancy(models.Model):
    title = models.CharField(max_length=250)
    advertiser = models.ForeignKey(Advertiser, related_name='vacancies', on_delete=models.CASCADE)
