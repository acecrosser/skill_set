from django.contrib import admin
from .models import MakeProfit, Expenses


@admin.register(MakeProfit)
class MakeProfitAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'created', 'author')
    date_hierarchy = 'created'


@admin.register(Expenses)
class MakeExpensesAdmin(admin.ModelAdmin):
    list_display = ('title', 'expenses', 'amount', 'created', 'author')

