from django.db import models

# Create your models here.


class Exchange(models.Model):
    name = models.TextField(null=False, unique=True)
    nickname = models.TextField()

    def __str__(self):
        return '{name} | {nickname}'.format(name=self.name, nickname=self.nickname)


class Company(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    name = models.TextField(null=False)
    ticker = models.TextField(null=False)
    ipo_year = models.IntegerField(null=True)
    sector = models.TextField()
    industry = models.TextField()

    class Meta:
        unique_together = ('exchange', 'ticker',)

    def __str__(self):
        return '{exchange} | {name} | {ticker}'.format(exchange=self.exchange, name=self.name, ticker=self.ticker)
