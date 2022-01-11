from django.db import models

# Create your models here.
class Customer(models.Model):
    
    customerName= models.CharField(max_length=50)
    accountNo= models.IntegerField(primary_key=True)
    UPI_ID= models.CharField(max_length=20)
    email= models.EmailField(max_length=30)
    balance=models.FloatField()
    mobile=models.CharField(max_length=10)

    def details(self):
        return self.accountNo


class transaction_history(models.Model):
    senderaccount = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name='sender')
    receiveraccount = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name='receiver')

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    amount = models.FloatField()

    def details(self):
        return self.senderaccount,self.receiveraccount,self.timestamp,self.amount