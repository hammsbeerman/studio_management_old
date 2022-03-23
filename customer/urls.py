from django.urls import path
from . import views

urlpatterns = [
    path('addcustomer', views.add_customer, name='add-customer'),
    path('customers', views.all_customers, name='all-customers'),
    path('customer_detail/<customer_id>', views.customer_detail, name='customer-detail'),
    path('contact_update/<contact_id>', views.contact_update, name='contact-update'),
    path('admin_approval', views.admin_approval, name='admin-approval'),
    path('customer_contact/<customer_id>', views.customer_contact, name='customer-contact'),
    path('contact_detail/<contact_id>', views.contact_detail, name='contact-detail'),
    path('addcontact', views.add_contact, name='add-contact'),
    #
    path('addcustomer_contact/<customer_id>', views.add_customer_contact, name='add-cust-contact'),
    path('customer_update/<customer_id>', views.customer_update, name='customer-update'),
]
