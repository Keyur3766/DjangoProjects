from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Customer, transaction_history
from django.contrib import messages
# Create your views here.
import logging




senderAccount="-1"
def index(request):
    return render(request,'index.html')



def customers(request):
    all_customers = Customer.objects.raw("SELECT * FROM public.home_customer")
    return render(request,'customers.html',{'all_customers':all_customers})


def transactions(request):
    all_customers = Customer.objects.raw("SELECT * FROM public.home_customer")
    return render(request,'transaction.html',{'all_customers':all_customers})   


def sender_Profile(request):
    all_customers = Customer.objects.raw("SELECT * FROM public.home_customer")
    if 'verify' in request.POST:   
        senderAccount = request.POST['senderAccountNo']

        if senderAccount == 'select Sender Account':
            messages.error(request, 'Sender not selected')
            return render(request,'transaction.html',{'all_customers':all_customers}) 
        selectedSender = Customer.objects.get(accountNo=senderAccount)

    if 'submitUPI' in request.POST:
        receiver_Account_no = request.POST['receiver_Account_no']
        amount = float(request.POST['Amount'])
        sender = request.POST['senderID']
        selectedSender = Customer.objects.get(accountNo=sender)
        selectedreceiver = Customer.objects.get(accountNo=receiver_Account_no)

        if amount>selectedSender.balance:
            messages.error(request, 'Insufficient balance in the account')

        else:
            selectedSender.balance = selectedSender.balance-amount
            selectedreceiver.balance = selectedreceiver.balance+amount

            selectedSender.save()
            selectedreceiver.save()

            transaction_money = transaction_history(senderaccount_id=sender, receiveraccount_id=receiver_Account_no, amount=amount)
            transaction_money.save()
            messages.success(request,'Payment Done Successfully')
        #return HttpResponse(sender)
    

    if 'submitAccount' in request.POST:
        receiver_Account_no = request.POST['receiver_Account_no']
        amount = float(request.POST['Amount'])
        sender = request.POST['senderID']
        selectedSender = Customer.objects.get(accountNo=sender)
        selectedreceiver = Customer.objects.get(accountNo=receiver_Account_no)

        if amount>selectedSender.balance:
            messages.error(request, 'Insufficient balance in the account')

        else:
            selectedSender.balance = selectedSender.balance-amount
            selectedreceiver.balance = selectedreceiver.balance+amount

            selectedSender.save()
            selectedreceiver.save()

            transaction_money = transaction_history(senderaccount_id=sender, receiveraccount_id=receiver_Account_no, amount=amount)
            transaction_money.save()
            messages.success(request,'Payment Done Successfully')
        #return HttpResponse(sender)

    return render(request,'transaction1.html',{'all_customers':all_customers, 'selectedSender':selectedSender})



def history(request):
    all_transactions = transaction_history.objects.all()
    return render(request,'history.html',{'all_transactions':all_transactions})



def customer_transaction(request, accountNo):
    #CustomerData = transaction_history.objects.raw("SELECT * FROM public.home_transaction_history WHERE senderaccount_id={accountNo} or receiveraccount_id={accountNo} ORDER BY timestamp DESC")

    CustomerData = (transaction_history.objects.filter(senderaccount=accountNo) | transaction_history.objects.filter(receiveraccount=accountNo)).order_by('timestamp').reverse()
    selectedSender = Customer.objects.get(accountNo=accountNo)
    return render(request,'customer_transaction.html',{'CustomerData':CustomerData,'accountNo':accountNo,'selectedSender':selectedSender})
    
    