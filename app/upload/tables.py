import django_tables2 as tables
from .models import Accounts

class AccountsTable(tables.Table):
    class Meta:
        model = Accounts
