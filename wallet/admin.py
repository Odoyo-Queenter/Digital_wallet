from django.contrib import admin

from .models import Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Receipt
from .models import Notification
from .models import Loan
from .models import Reward


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','address','email','phone_number','gender','age')
    search_fields =('first_name','last_name','address','email','phone_number','gender','age')
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_dispaly = ('customer','amount','currency')
    search_fields = ('customer','amount','currency')
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name','account_number') 
    search_fields = ('account_name','account_number') 
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_amount','transaction_type','date_and_time','transaction_code')
    search_fields =  ('transaction_amount','transaction_type',' date_and_time','transaction_code')
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_account','card_number')
    Search_fields = ('card_account','card_number')
admin.site.register(Card,CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ('account_number',"transaction_cost")
    search_fields = ('account_number','transaction_cost')
admin.site.register(ThirdParty,ThirdPartyAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_type','receipt_date','receipt_number','total_amount')
    search_fields =(' receipt_type','receipt_date','receipt_number','total_amount')
admin.site.register(Receipt,ReceiptAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display =('tittle','date_of_notification')
    search_fields= ('tittle','date_of_notification')
admin.site.register(Notification,NotificationAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('amount','date_time')
    search_fields = ('amount','date_time')
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display  = ('customer_id','transacation','date_reward','receipt')
    search_fields = ('customer_id','transacation','date_reward','receipt')
admin.site.register(Reward,RewardAdmin)
