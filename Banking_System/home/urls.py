from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('customers',views.customers,name="customers"),
    path('transactions',views.transactions,name="transactions"),
    path('sender_Profile',views.sender_Profile,name="sender_Profile"),
    path('history',views.history,name="history"),
    path('customers/customer_transaction/<accountNo>',views.customer_transaction,name="customer_transaction")
]
