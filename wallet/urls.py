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
    path("notifications/",views.list_notifications,name = "notifications_list"),
    path("accounts/",views.list_accounts,name = "accounts_list"),
    path("wallets/",views.list_wallets,name = "wallets_list"),
    path("transactions",views.list_transactions,name = "trasactions_list"),
    path("cards",views.list_cards,name = "cards_list"),
    path("thirdPartys",views.list_thirdPartys,name = "thirdPartys_list"),
    path("receipts",views.list_receipts,name = "receipts_list"),
    path("loans",views.list_loans,name = "loans_list"),
    path("rewards",views.list_rewards,name = "rewards_list")


]