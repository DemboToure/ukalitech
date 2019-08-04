from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounting_home, name='accountingHome'),
    path('accounting_account', views.accounting_account, name='accountingAccount'),
    path('accounting_journal', views.accounting_journal, name='accountingJournal'),
    path('accounting_book', views.accounting_book, name='accountingBook'),
]
