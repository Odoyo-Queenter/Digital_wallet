from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.cxx
class Customer(models.Model):
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    address = models.TextField(null=True)
    email=models.EmailField(default=False)
    phone_number= models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=10,null=True)
    age = models.SmallIntegerField(null=True)


class Account(models.Model):
    account_name = models.CharField(max_length=20,null=True)
    account_number = models.IntegerField()
    balance = models.BigIntegerField()
    account_pin = models.PositiveIntegerField(null=True)
    currency = models.CharField(max_length=20,null=True)



class Wallet(models.Model):
    balance = models.BigIntegerField()
    customer = models.ForeignKey(on_delete=models.CASCADE, to=Customer,null=True)
    amount = models.BigIntegerField()
    date_created = models.DateTimeField(default=datetime.now)
    currency = models.CharField(max_length=20,null=True)
    account = models.ForeignKey(on_delete=models.CASCADE, to=Account,null=True)
    account_pin = models.SmallIntegerField(null=True)

class Transaction(models.Model):
    transaction_code = models.IntegerField()
    Wallet = models.ForeignKey(on_delete=models.CASCADE, to=Wallet,null=True)
    transaction_amount = models.BigIntegerField()
    transaction_type = models.CharField(max_length=20,null=True)
    date_and_time = models.DateTimeField(default=datetime.now)
    origin_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_a",null=True)
    destination_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="accountb",null=True)

class  Card(models.Model):
    card_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_e",null=True)
    card_number = models.IntegerField()
    card_holder_name = models.CharField(max_length=27,null=True)
    Wallet = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_f",null=True)
    expiry_date = models.DateTimeField(default=datetime.now)
    date_issued = models.DateTimeField(default=datetime.now)
    card_type = models.CharField(max_length=25,null=True)


class ThirdParty(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_c",null=True)
    account_number = models.IntegerField(null=True)
    transaction_cost = models.IntegerField()
    currency = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_d",null=True)

class Receipt(models.Model):
    receipt_type = models.CharField(max_length=22,null=True)
    receipt_date =  models.DateTimeField(default=datetime.now)
    receipt_number = models.BigIntegerField()
    total_amount = models.IntegerField()
    transaction = models.ForeignKey(on_delete=models.CASCADE,to=Transaction,null=True)
    receipt_file = models.FileField() 


class Notification(models.Model):
    message = models.CharField(max_length=50,null=True)
    tittle = models.CharField(max_length=25,null=True)
    date_of_notification = models.DateTimeField(default=datetime.now)
    recipient = models.ForeignKey(on_delete=models.CASCADE,to=Receipt,null=True)
    state = (
        ('a', 'active'),
        ('in','inactive')

    )
    status = models.CharField( max_length=10,choices=state, null=True)

class Loan(models.Model):
    amount = models.BigIntegerField()
    loan_type = models.CharField(max_length=20,null=True)
    interest_rate = models.PositiveIntegerField()
    date_time = models.DateTimeField(default=datetime.now)
    loan_id = models.SmallIntegerField(null=True)
    wallet = models.ForeignKey(on_delete=models.CASCADE,to=Wallet,null=True)   


class Reward(models.Model):
    receipt = models.ForeignKey(on_delete=models.CASCADE,to=Receipt,null=True)
    transacation = models.ForeignKey(on_delete=models.CASCADE,to=Transaction,null=True)
    customer_id = models.IntegerField(null=True)
    date_reward = models.DateTimeField(default=datetime.now)






  
