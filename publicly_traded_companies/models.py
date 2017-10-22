from django.db import models

# Create your models here.


class Exchange(models.Model):
    name = models.TextField(null=False, unique=True)
    nickname = models.TextField()

    def __str__(self):
        return '{name} | {nickname}'.format(name=self.name, nickname=self.nickname)


class Industry(models.Model):
    name = models.TextField(null=True)


class Sector(models.Model):
    name = models.TextField(null=True)


class Company(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    name = models.TextField(null=False)
    ticker = models.TextField(null=False)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    address_line_1 = models.TextField(null=True)
    address_line_2 = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    country = models.TextField(null=True)
    zip_code = models.TextField(null=True)
    fax_number = models.TextField(null=True)
    phone_number = models.TextField(null=True)
    website_url = models.URLField(null=True)
    employee_count = models.IntegerField(null=True)
    business_summary = models.TextField(null=True)

    class Meta:
        unique_together = ('exchange', 'ticker',)

    def __str__(self):
        return '{exchange} | {name} | {ticker}'.format(exchange=self.exchange, name=self.name, ticker=self.ticker)
