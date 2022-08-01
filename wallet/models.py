from datetime import datetime
import email
from locale import currency
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField()
    email=models.EmailField()
    phone_number= models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()


class Account(models.Model):
    account_name = models.CharField(max_length=20)
    account_number = models.IntegerField()
    balance = models.BigIntegerField()
    account_pin = models.PositiveIntegerField()
    currency = models.CharField(max_length=20)
    


class Wallet(models.Model):
    balance = models.BigIntegerField()
    Customer = models.ForeignKey(on_delete=models.CASCADE, to=Customer)
    amount = models.BigIntegerField()
    date_created = models.DateTimeField(default=datetime.now)
    currency = models.CharField(max_length=20)
    account = models.ForeignKey(on_delete=models.CASCADE, to=Account)
    account_pin = models.PositiveIntegerField()

class Transaction(models.Model):
    transaction_code = models.IntegerField()
    Wallet = models.ForeignKey(on_delete=models.CASCADE, to=Wallet)
    transaction_amount = models.BigIntegerField()
    transaction_type = models.CharField(max_length=20)
    date_and_time = models.DateTimeField(default=datetime.now)
    origin_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_a")
    destination_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="accountb")

class  Card(models.Model):
    card_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_e")
    card_number = models.IntegerField()
    card_holder_name = models.CharField(max_length=25)
    Wallet = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_f")
    expiry_date = models.DateTimeField(default=datetime.now)
    date_issued = models.DateTimeField(default=datetime.now)
    card_type = models.CharField(max_length=25)


class ThirdParty(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_c")
    account_number = models.BigIntegerField()
    transaction_cost = models.BigIntegerField()
    currency = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_d")

class Receipt(models.Model):
    receipt_type = models.CharField(max_length=22)
    receipt_date =  models.DateTimeField()
    receipt_number = models.BigIntegerField()
    total_amount = models.IntegerField()
    transaction = models.ForeignKey(on_delete=models.CASCADE,to=Transaction)
    receipt_file = models.FileField() 


class Notification(models.Model):
    message = models.CharField(max_length=50)
    tittle = models.CharField(max_length=25)
    date_time = models.DateTimeField()
    recipient = models.ForeignKey(on_delete=models.CASCADE,to=Receipt)
    state = (
        ('a', 'active'),
        ('in','inactive')

    )
    status = models.CharField( max_length=10,choices=state, null=True)

class Loan(models.Model):
    amount = models.BigIntegerField()
    loan_type = models.CharField(max_length=20)
    interest_rate = models.PositiveIntegerField()
    date_time = models.DateTimeField(default=datetime.now)
    loan_id = models.SmallIntegerField()
    wallet = models.ForeignKey(on_delete=models.CASCADE,to=Wallet)   


class Reward(models.Model):
    receipt = models.ForeignKey(on_delete=models.CASCADE,to=Receipt)
    transacation = models.ForeignKey(on_delete=models.CASCADE,to=Transaction)
    customer_id = models.IntegerField()
    date_reward = models.DateTimeField(default=datetime.now)
     



    


    

