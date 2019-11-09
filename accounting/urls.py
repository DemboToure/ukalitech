from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounting_home, name='accountingHome'),
    path('accounting_account', views.accounting_account, name='accountingAccount'),
    path('accounting_journal', views.accounting_journal, name='accountingJournal'),
    path('accounting_book', views.accounting_book, name='accountingBook'),
    path('accounting_bilan', views.accounting_bilan, name='accountingBilan'),
    path('accounting_balance', views.accounting_balance, name='accountingBalance'),
    path('accounting_result', views.accounting_result, name='accountingResult'),
    path('accounting_import', views.accounting_import, name='accountingImport'),

]
