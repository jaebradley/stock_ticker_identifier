from django.db import models

# Create your models here.


class Exchange(models.Model):
    name = models.TextField(null=False, unique=True)
    nickname = models.TextField()


class Company(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    name = models.TextField(null=False)
    ticker = models.TextField(null=False)
    ipo_year = models.IntegerField(null=True)
    sector = models.TextField()
    industry = models.TextField()

    class Meta:
        unique_together = ('exchange', 'ticker',)
