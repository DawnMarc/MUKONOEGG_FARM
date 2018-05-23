# Create your models here.

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Orders(models.Model):
    user = models.ForeignKey('auth.User', blank=True, null=True)
    Prices = models.ForeignKey('Prices', blank=True, null=True)
    order_no = models.AutoField(primary_key=True)
    no_of_trays = models.IntegerField(null=False, default=0)
    location = models.CharField(max_length=100, default='current location')
    request_date = models.DateTimeField(default=timezone.now)
    total_amt_due = models.FloatField(default=0.000, max_length=100, null=False)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.location


class Invoice(models.Model):
    invoice_no = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User')
    prices = models.ForeignKey('Prices')
    orders = models.ForeignKey('Orders')

    def invoice_unique(self):
        return self.invoice_no


class Prices(models.Model):
    Px_per_Egg = models.PositiveIntegerField()
    eggs_in_tray = models.PositiveIntegerField(default=24)
    Date = models.DateTimeField(default=timezone.now)
    Px_per_Tray = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        try:
            self.Px_per_Tray = self.Px_per_Egg * self.eggs_in_tray
        except TypeError:
            pass
        super(Prices, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.Px_per_Tray)


class Capacity(models.Model):
    no_of_trays = models.CharField(max_length=50)
    damaged = models.IntegerField()
    Date = models.DateTimeField(default=timezone.now)

    def tray(self):
        return self.no_of_trays

    def damaged_eggs(self):
        return self.str_damaged
