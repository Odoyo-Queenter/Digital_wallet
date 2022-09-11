from pathlib import Path
from unicodedata import name
from django.urls import path
from . import views
from .views import register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet

urlpatterns = [
    path("register/",register_customer,name ="registration"),
    path("account/",register_account,name ="account"),
    path("wallet/",register_wallet,name ="wallet"),
    path("transaction/",register_transaction,name ="transaction"),
    path("card/",register_card,name ="card"),
    path("thirdparty/",register_thirdparty,name ="thirdparty"),
    path("receipt/",register_receipt,name ="receipt"),
    path("notification/",register_notification,name ="notification"),
    path("loan/",register_loan,name ="loan"),
    path("reward/",register_reward,name ="reward"),
    path("customers/",views.list_customers,name ="customers_list"),
    path("notification/",views.list_notification,name = "notification_list"),
    path("account/",views.list_account,name = "account_list"),
    path("wallet/",views.list_wallet,name = "wallet_list"),
    path("transaction",views.list_wallet,name = "trasaction_list"),
    path("card",views.list_card,name = "card_list"),
    path("thirdParty",views.list_thirdParty,name = "thirdParty_list"),
    path("receipt",views.list_receipt,name = "receipt_list"),
    path("loan",views.list_loan,name = "loan_list"),
    path("reward",views.list_reward,name = "reward_list")


]