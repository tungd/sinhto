from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
