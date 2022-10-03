from pathlib import Path
from unicodedata import name
from django.urls import path
from . import views
from .views import account_profile, card_profile, customers_profile, edit_account, edit_customer, edit_receipt, edit_wallet, receipt_profile, register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet, transaction_profile, wallet_profile

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
    path("rewards",views.list_rewards,name = "rewards_list"),

    path("customers/<int:id>/",customers_profile,name ="customers_profile"),
    path("customers/edit/<int:id/",edit_customer,name= "edit_customer"),
    path("wallet/<int:id>/",wallet_profile,name="wallet_profile"),
    path("wallet/edit/<int:id>/",edit_wallet,name= "edit_wallet"),
    path("account/<int:id>/",account_profile,name="account_profile"),
    path("account/edit/<int:id>/",edit_account,name="edit_account"),
    path("card/<int:id>/",card_profile,name="card_profile"),
    path("card/edit/<int:id>/",edit_account,name="edit_card"),
    path("transaction/<int:id>/",transaction_profile,name="transaction_profile"),
    path("transaction/edit/<int:id>/",edit_account,name="edit_transaction"),
    path("receipt/<int:id>/",receipt_profile,name="receipt_profile"),
    path("receipt/edit/<int:id>/",edit_receipt,name="edit_receipt")
  



]  