from django.db import models

class Inventory(models.Model):
    internal_part_number = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)
    qty_ordered = models.IntegerField(blank=True)
    cost = models.IntegerField(blank=True)
    total = models.IntegerField(blank=True)
    qty_sold = models.IntegerField(blank=True)
    sell_price = models.IntegerField(blank=True)
    total = models.IntegerField(blank=True)

    def __str__(self):
        return self.internal_part_number
