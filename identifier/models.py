from django.db import models
from django_elasticsearch.models import EsIndexable

# Create your models here.


class Company(EsIndexable, models.Model):
    name = models.TextField(null=False)
    ticker = models.TextField(null=False)
    ipo_year = models.IntegerField()
    sector = models.TextField()
    industry = models.TextField()