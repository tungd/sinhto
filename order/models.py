from django.db import models


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE
    )
    drink = models.ForeignKey(
        'inventory.Drink', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{drink} - {name}'.format(
            drink=self.drink, name=self.name
        )
