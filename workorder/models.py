from django.db import models
from customer.models import Customer, Contact
from inventory.models import Inventory




class Workorder(models.Model):
    workorder = models.CharField('Workorder', max_length=20, blank=False)
    date = models.DateField('Time In', null=True)
    organization = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL, related_name='workorder_customer')
    ##organization = models.CharField('Organiation', max_length=100, blank=True)
    contact = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.SET_NULL, related_name='workorder_contact')
    description = models.CharField('Description', max_length=250, blank=True)
    deadline = models.DateTimeField('Deadline', null=True, blank=True)
    budget = models.IntegerField('Budget', null=True, blank=True)
    quoted_price = models.IntegerField('Quoted Price', null=True, blank=True)
    material = models.ManyToManyField(Inventory, blank=True)
    #workorder_material = models.ForeignKey(Testing)
    #workorder_material = models.ForeignKey(Testitem, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.workorder
