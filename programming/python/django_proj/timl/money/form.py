from django import forms
from .models import MakeProfit, Expenses


class MakeProfitForm(forms.ModelForm):
    class Meta:
        model = MakeProfit
        fields = ('title', 'amount',)


class MakeExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('title', 'amount',)
