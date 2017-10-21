from django.db import models

# Create your models here.


class Exchange(models.Model):
    name = models.TextField(null=False, unique=True)
    nickname = models.TextField()

    def __str__(self):
        return '{name} | {nickname}'.format(name=self.name, nickname=self.nickname)


class Industry(models.Model):
    name = models.TextField(null=False)


class Sector(models.Model):
    name = models.TextField(null=False)


class Company(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    name = models.TextField(null=False)
    ticker = models.TextField(null=False)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    address_line_1 = models.TextField()
    address_line_2 = models.TextField()
    city = models.TextField()
    state = models.TextField()
    country = models.TextField()
    zip_code = models.TextField()
    fax_number = models.TextField()
    phone_number = models.TextField()
    website_url = models.URLField()
    employee_count = models.IntegerField()
    business_summary = models.TextField()

    class Meta:
        unique_together = ('exchange', 'ticker',)

    def __str__(self):
        return '{exchange} | {name} | {ticker}'.format(exchange=self.exchange, name=self.name, ticker=self.ticker)
