from django.shortcuts import render, get_object_or_404
from .models import MakeProfit, Expenses
from .form import MakeProfitForm, MakeExpensesForm
from django.db.models import Sum
from django.views.generic import View


def make_money(request):
    obj_data = MakeProfit.objects.filter(author=request.user)
    expenses_data = Expenses.objects.filter(author=request.user)
    # сумирует весь профит юзера
    amount_user = MakeProfit.objects.filter(author=request.user).aggregate(Sum('amount'))
    # obj_data = get_object_or_404(MakeProfit, author=author)
    # expenses_data = get_object_or_404(Expenses, author=author)
    new_profit = None
    new_expenses = None
    if request.method == 'POST' and 'profit' in request.POST:
        make_profit = MakeProfitForm(data=request.POST)
        if make_profit.is_valid():
            new_profit = make_profit.save(commit=False)
            new_profit.author = request.user
            new_profit.save()
    else:
        make_profit = MakeProfitForm()

    if request.method == 'POST' and 'expense' in request.POST:
        make_expenses = MakeExpensesForm(data=request.POST)
        if make_expenses.is_valid():
            new_expenses = make_expenses.save(commit=False)
            new_expenses.author = request.user
            new_expenses.save()
    else:
        make_expenses = MakeExpensesForm()

    return render(request, 'money/make_money.html', {'obj_data': obj_data,
                                                     'new_profit': new_profit,
                                                     'make_profit': make_profit,
                                                     'new_expenses': new_expenses,
                                                     'make_expenses': make_expenses,
                                                     'expenses_data': expenses_data,
                                                     # amount__sum - ключ который возвращает джанго
                                                     'amount_user': amount_user.pop('amount__sum')})


# class MakeMoney(View):
#
#     def make_money(self, request):
#         obj_data = MakeProfit.objects.filter(author=request.user)
#         new_profit = None
#         if request.method == 'POST':
#             make_profit = MakeProfitForm(data=request.POST)
#             if make_profit.is_valid():
#                 new_profit = make_profit.save(commit=False)
#                 new_profit.author = request.user
#                 new_profit.save()
#         else:
#             make_profit = MakeProfitForm()
#         return render(request, 'money/make_money.html', {'obj_data': obj_data,
#                                                          'new_profit': new_profit,
#                                                          'make_profit': make_profit,})
#
#     def make_expenses(self, request):
#         expenses_data = Expenses.objects.filter(author=request.user)
#         new_expenses = None
#         if request.method == 'POST':
#             make_expenses = MakeExpensesForm(data=request.POST)
#             if make_expenses.is_valid():
#                 new_expenses = make_expenses.save(commit=False)
#                 new_expenses.author = request.user
#                 new_expenses.save()
#         else:
#             make_expenses = MakeExpensesForm()
#         return render(request, 'money/make_money.html', {'expenses_data': expenses_data,
#                                                          'new_expense': new_expenses,
#                                                          'make_expenses': make_expenses,})
#
#     def sum_profit(self, request):
#         amount_user = MakeProfit.objects.filter(author=request.user).aggregate(Sum('amount'))
#         return render(request, 'money/make_money.html', {'amount_user': amount_user.pop('amount__sum')})





