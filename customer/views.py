from django.shortcuts import render, redirect
from .forms import CustomerForm, CustomerContactForm, SingleCustomerContactForm
from django.http import HttpResponseRedirect
from .models import Customer, Contact
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User

def add_customer(request):
    submitted = False
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/customer/addcustomer?submitted=True')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'customers/addcustomer.html',{'form':form, 'submitted':submitted})

def all_customers(request):
    all_customers = Customer.objects.all().order_by('name')
    return render(request, 'customers/all_customers.html',
        {'all_customers': all_customers})

def customer_detail(request, customer_id):
    customer_info = Customer.objects.get(pk=customer_id)
    return render(request, 'customers/customer_detail.html',
        {'customer_info': customer_info,})

def customer_update(request, customer_id):
    customer_info = Customer.objects.get(pk=customer_id)
    update_form = CustomerForm(request.POST or None, instance=customer_info)
    if update_form.is_valid():
        update_form.save()
        return redirect('all-customers')
    return render(request, 'customers/update_customer.html',
        {
        'customer_info': customer_info,
        'update_form': update_form,
        })

#Admin Approval Page
def admin_approval(request):
    #Get the customers
    customer_list = Customer.objects.all()
    #Count Customers and contacts
    customer_count = Customer.objects.all().count()
    contact_count = Contact.objects.all().count()
    user_count = User.objects.all().count()
    contact_list = Contact.objects.all().order_by('-lname')
    if request.user.is_superuser:
        if request.method == "POST":
            #Gather the id for the boxes that have been checked
            id_list = request.POST.getlist('boxes')
            #Uncheck all contacts - Hack to unapprove contacts
            contact_list.update(approved=False)
            #convert x to intiger and update database
            for x in id_list:
                Contact.objects.filter(pk=int(x)).update(approved=True)
            messages.success(request, ("Approvals updated"))
            return redirect('all-customers')
        else:
            return render(request, 'customers/admin_approval.html',
            {
            'contact_list': contact_list,
            'customer_count': customer_count,
            'contact_count': contact_count,
            'user_count': user_count,
            'customer_list': customer_list
            })
    else:
        messages.success(request, ("You are not authorized"))
        return redirect('home')

def customer_contact(request, customer_id):
    #Get the Customer
    customer = Customer.objects.get(id=customer_id)
    #Get the contacts
    contacts = customer.contact_set.all()
    if contacts:
        return render(request, 'customers/customer_contact.html',
            {
            'contacts': contacts
            })
    else:
        messages.success(request, ("No Contact info for this company"))
        return redirect('admin-approval')

def contact_detail(request, contact_id):
    contact_detail = Contact.objects.get(pk=contact_id)
    return render(request, 'customers/contact_detail.html',
        {
        'contact_detail': contact_detail
        })

def add_contact(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = CustomerContactForm(request.POST)
        else:
            form = SingleCustomerContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/customer/addcontact?submitted=True')
    else:
        if request.user.is_superuser:
            form = CustomerContactForm
        else:
            form = SingleCustomerContactForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'customers/addcustomer_contact.html',{'form':form, 'submitted':submitted})

def contact_update(request, contact_id):
    contact_info = Contact.objects.get(pk=contact_id)
    update_form = CustomerContactForm(request.POST or None, instance=contact_info)
    if update_form.is_valid():
        update_form.save()
        #print("update_form", update_form.cleaned_data)
        return redirect('admin-approval')
    return render(request, 'customers/update_contact.html',
        {
        'contact_info': contact_info,
        'update_form': update_form,
        })

def add_customer_contact(request, customer_id):
    if request.method == "POST":
        customer_info = Customer.objects.get(pk=customer_id)
        form = CustomerContactForm(request.POST)
        if form.is_valid():
            addcontact = form.save(commit=False)
            addcontact.customer = customer_info.Name
            addcontact.save()
            print("addcontact", addcontact.cleaned_data)
            #return HttpResponseRedirect('customers/admin_approval.html')
        else:
            form = SingleCustomerContactForm
            if 'submitted' in request.GET:
                submitted = True
                return render(request, 'customers/addcustomer_contact.html',{'form':form, 'submitted':submitted})



##This works as is for adding contact
#def add_contact(request):
#    submitted = False
#    if request.method == "POST":
#        form = CustomerContactForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/customer/addcontact?submitted=True')
#    else:
#        form = CustomerContactForm
#        if 'submitted' in request.GET:
#            submitted = True
#        return render(request, 'customers/addcustomer_contact.html',{'form':form, 'submitted':submitted})
##End of contact form



#def add_customer_contact(request, customer_id):
#    contact_info = Customer.objects.get(pk=customer_id)
#    update_form = CustomerContactForm(request.POST or None, instance=contact_info)
#    if update_form.is_valid():
#        update_form.save()
#        return redirect('all-customers')
#    return render(request, 'customers/addcustomer_contact.html',
#        {
#        'contact_info': contact_info,
#        'update_form': update_form,
#        })





#This section is listing two seperate forms in the same submitted
#Not used, but may be good for future reference
#def new_customer(request):
#    form = CustomerForm(request.POST)
#    form2 = CustomerContactForm(request.POST)
#    context = {
#        'form': form,
#        'form2': form2,
#    }
#    if all([form.is_valid(), form2.is_valid()]):
#        #obj = form.save(commit=False)
#        #obj.user = request.user
#        #obj.save()
#        form.save(commit=True)
#        form2.save(commit=True)
#        print("form", form.cleaned_data)
#        print("form2", form2.cleaned_data)
#    return render(request, 'customers/newcustomer.html', context)
