from django.shortcuts import render
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Transaction, Wallet
from . import forms
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.
def register_customer(request):
    if request.method =='POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerRegistrationForm()        
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{'form':form})


def list_customers(request):
    customers = Customer.objects.all() 
    return render(request,'wallet/customers_list.html',{"customers":customers})      

def register_account(request):
    if request.method =='POST':
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountRegistrationForm()       
    form = AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{'form':form})


def list_account(request):
    account = Account.objects.all() 
    return render(request,'wallet/account_list.html',{"account":account})      


def register_wallet(request):
    if request.method =='POST':
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WalletRegistrationForm()        
    form = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{'form':form}) 


def list_wallet(request):
    wallet = Wallet.objects.all() 
    return render(request,'wallet/wallet_list.html',{"wallet":wallet})      


def register_transaction(request):
    if request.method =='POST':
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()        
    form = TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{'form':form}) 


def list_transaction(request):
    transaction = Transaction.objects.all() 
    return render(request,'wallet/transaction_list.html',{"transaction":transaction})      


def register_card(request):
    if request.method =='POST':
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CardRegistrationForm()        
    form = CardRegistrationForm()
    return render(request,"wallet/register_card.html",{'form':form})  


def list_card(request):
    card = Card.objects.all() 
    return render(request,'wallet/card_list.html',{"card":card})      

def register_thirdparty(request):
    if request.method =='POST':
        form = ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ThirdPartyRegistrationForm()        
    form = ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{'form':form}) 


def list_thirdParty(request):
    thirdParty= thirdParty.objects.all() 
    return render(request,'wallet/thirdParty_list.html',{"thirdParty":thirdParty})     

def register_receipt(request):
    if request.method =='POST':
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReceiptRegistrationForm()        
    form = ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{'form':form})

def list_receipt(request):
    receipt= Receipt.objects.all() 
    return render(request,'wallet/receipt_list.html',{"receipt":receipt})     


def register_notification(request):
    if request.method =='POST':
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NotificationRegistrationForm()        
    form = NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",{'form':form}) 


def list_notification(request):
    notification = Notification.objects.all() 
    return render(request,'wallet/notification_list.html',{"notification":notification})      

def register_loan(request):
    if request.method =='POST':
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoanRegistrationForm()        
    form = AccountRegistrationForm()
    return render(request,"wallet/register_loan.html",{'form':form}) 


def list_loan(request):
    loan= Loan.objects.all() 
    return render(request,'wallet/loan_list.html',{"loan":loan})     


def register_reward(request):
    if request.method =='POST':
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =RewardRegistrationForm()        
    form = RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{'form':form}) 


def list_reward(request):
    reward= Reward.objects.all() 
    return render(request,'wallet/reward_list.html',{"reward":reward})    

