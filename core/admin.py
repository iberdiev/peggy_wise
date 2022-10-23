from django.contrib import admin
from .models import Category, PiggyBank, Transaction, UserSavings
# Register your models here.



admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(PiggyBank)
admin.site.register(UserSavings)
