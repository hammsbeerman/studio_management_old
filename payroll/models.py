from django.db import models

class Timecard(models.Model):
    Description = (
        ('D', 'Design'),
        ('L', 'Lunch'),
        ('O', 'Officework'),
        ('P', 'Personal'),
        ('X', 'Other'),
    )
    employee = models.CharField('Employee', max_length=20)
    timein = models.DateTimeField('Time In')
    timeout = models.DateTimeField('Time Out')
    description = models.CharField('Description', max_length=1, choices=Description)
    billable = models.CharField('Billable', max_length=10)
    jobnumber = models.CharField('Job Number', max_length=10)

    def __str__(self):
        return self.employee
