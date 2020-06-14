from django.contrib import admin

from .models import Company, Accounts,Category,SicCode

admin.site.register(Company)
admin.site.register(Accounts)
admin.site.register(Category)
admin.site.register(SicCode)
