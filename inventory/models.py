from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Drink(models.Model):
    shop = models.ForeignKey(
        Shop, related_name='drinks', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=0)

    def __str__(self):
        return self.name
