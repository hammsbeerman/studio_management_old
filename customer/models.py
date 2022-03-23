from django.db import models

class Customer(models.Model):
    name = models.CharField('Name', max_length=100, blank=False, null=True)
    address1 = models.CharField('Address 1', max_length=100, blank=True, null=True)
    address2 = models.CharField('Adddress 2', max_length=100, blank=True, null=True)
    city = models.CharField('City', max_length=100, null=True)
    state = models.CharField('State', max_length=100, null=True)
    zipcode = models.CharField('Zipcode', max_length=100, blank=True, null=True)
    phone1 = models.CharField('Phone 1', max_length=100, blank=True, null=True)
    phone2 = models.CharField('Phone 2', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)
    website = models.URLField('Website', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        #self.name = self.name.lower().capitalize()
        self.name = self.name.title()
        self.city = self.city.title()
        self.state = self.state.title()
        super(Customer, self).save( *args, **kwargs) # Call the "real" save() method.
        #do_something_else()

class Contact(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    #company = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True, null=True)
    fname = models.CharField('Name', max_length=100, blank=True, null=True)
    lname = models.CharField('Name', max_length=100, blank=True, null=True)
    phone1 = models.CharField('Phone 1', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)
    approved = models.BooleanField('Approved', default=False)

    def __str__(self):
        return self.fname

    def save(self, *args, **kwargs):
        #self.name = self.name.lower().capitalize()
        self.fname = self.fname.title()
        self.lname = self.lname.title()
        super(Contact, self).save( *args, **kwargs) # Call the "real" save() method.
        #do_something_else()
