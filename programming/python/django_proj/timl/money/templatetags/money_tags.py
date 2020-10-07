from django import template
from ..models import MakeProfit
from django.contrib.auth.models import User
from django.shortcuts import render

register = template.Library()


# @register.simple_tag
# def summa_profit():
#     obj_data = MakeProfit.objects.exclude(amount__exact=None).values('amount')
#     amount_sum = []
#     for amount in obj_data:
#         amount_sum += amount.values()
#     return sum(amount_sum)

