from urllib import request
from django.shortcuts import render,redirect
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
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
    customers =  Customer.objects.all() 
    return render(request,'wallet/customers_list.html',{"customers":customers}) 

def customers_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,'wallet/customers_profile.html',{"customer":customer})

def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.method =="POST":
        form = CustomerRegistrationForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()

    else:
        form = CustomerRegistrationForm(instance=customer)
    return render(request,"wallet/edit_customer.html",{"form":form})   


def register_account(request):
    if request.method =='POST':
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountRegistrationForm()       
    form = AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{'form':form})


def list_accounts(request):
    accounts = Account.objects.all() 
    return render(request,'wallet/accounts_list.html',{"accounts":accounts}) 


def account_profile(request,id):
    account = Wallet.objects.get(id=id)
    return render(request,'wallet/account_profile.html',{"account":account})

def edit_account(request, id):
    account= Account.objects.get(id=id)
    if request.method =="POST":
        form = AccountRegistrationForm(request.POST, instance=account)

        if form.is_valid():
            form.save()

    else:
        form = AccountRegistrationForm(instance=account)
    return render(request,"wallet/edit_account.html",{"form":form})   



def register_wallet(request):
    if request.method =='POST':
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WalletRegistrationForm()        
    form = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{'form':form}) 



def wallet_profile(request,id):
    wallet = Wallet.objects.get(id=id)
    return render(request,'wallet/wallet_profile.html',{"wallet":wallet})

def edit_wallet(request, id):
    wallet = Wallet.objects.get(id=id)
    if request.method =="POST":
        form = WalletRegistrationForm(request.POST, instance=wallet)

        if form.is_valid():
            form.save()

    else:
        form = WalletRegistrationForm(instance=wallet)
    return render(request,"wallet/edit_wallet.html",{"form":form})   



def list_wallets(request):
    wallets = Wallet.objects.all() 
    return render(request,'wallet/wallets_list.html',{"wallets":wallets})      


def register_transaction(request):
    if request.method =='POST':
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()        
    form = TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{'form':form}) 


def list_transactions(request):
    transactions = Transaction.objects.all() 
    return render(request,'wallet/transactions_list.html',{"transactions":transactions})      


def register_card(request):
    if request.method =='POST':
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CardRegistrationForm()        
    form = CardRegistrationForm()
    return render(request,"wallet/register_card.html",{'form':form})  


def list_cards(request):
    cards = Card.objects.all() 
    return render(request,'wallet/cards_list.html',{"cards":cards})  



def card_profile(request,id):
    card = Card.objects.get(id=id)
    return render(request,'wallet/card_profile.html',{"card":card})

def edit_card(request, id):
    card= Card.objects.get(id=id)
    if request.method =="POST":
        form = CardRegistrationForm(request.POST, instance=card)

        if form.is_valid():
            form.save()

    else:
        form = CardRegistrationForm(instance=card)
    return render(request,"wallet/edit_card.html",{"form":form})   


def register_thirdparty(request):
    if request.method =='POST':
        form = ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ThirdPartyRegistrationForm()        
    form = ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{'form':form}) 


def list_thirdPartys(request):
    thirdPartys= ThirdParty.objects.all() 
    return render(request,'wallet/thirdPartys_list.html',{"thirdPartys":thirdPartys})     

def register_receipt(request):
    if request.method =='POST':
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReceiptRegistrationForm()        
    form = ReceiptRegistrationForm()
    return render(request,"wallet/receipt_register.html",{'form':form})

def list_receipts(request):
    receipts= Receipt.objects.all() 
    return render(request,'wallet/receipts_list.html',{"receipts":receipts})  


def receipt_profile(request,id):
    receipt= Receipt.objects.get(id=id)
    return render(request,'wallet/receipt_profile.html',{"receipt":receipt})

def edit_receipt(request, id):
    receipt= Receipt.objects.get(id=id)
    if request.method =="POST":
        form = ReceiptRegistrationForm(request.POST, instance=receipt)

        if form.is_valid():
            form.save()

    else:
        form =ReceiptRegistrationForm(instance=receipt)
    return render(request,"wallet/edit_receipt.html",{"form":form})          



def register_notification(request):
    if request.method =='POST':
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NotificationRegistrationForm()        
    form = NotificationRegistrationForm()
    return render(request,"wallet/notification_register.html",{'form':form}) 


def list_notifications(request):
    notifications = Notification.objects.all() 
    return render(request,'wallet/notifications_list.html',{"notifications":notifications}) 


def transaction_profile(request,id):
    transaction= Transaction.objects.get(id=id)
    return render(request,'wallet/transaction_profile.html',{"transaction":transaction})

def edit_transacion(request, id):
    transaction= Transaction.objects.get(id=id)
    if request.method =="POST":
        form = TransactionRegistrationForm(request.POST, instance=transaction)

        if form.is_valid():
            form.save()

    else:
        form = TransactionRegistrationForm(instance=transaction)
    return render(request,"wallet/edit_transaction.html",{"form":form})          

def register_loan(request):
    if request.method =='POST':
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoanRegistrationForm()        
    form = AccountRegistrationForm()
    return render(request,"wallet/register_loan.html",{'form':form}) 


def list_loans(request):
    loans= Loan.objects.all() 
    return render(request,'wallet/loans_list.html',{"loans":loans})     


def register_reward(request):
    if request.method =='POST':
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =RewardRegistrationForm()        
    form = RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{'form':form}) 


def list_rewards(request):
    rewards= Reward.objects.all() 
    return render(request,'wallet/rewards_list.html',{"rewards":rewards})    

