from django.db import models
from django.contrib.auth.models import User


class MakeProfit(models.Model):
    title = models.CharField(max_length=150)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    # CASCADE удалит все, что связанно с юзером (после удаления юзвера)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f'Profit from {self.title}: {self.amount}'


class Expenses(models.Model):

    CONSTANT_EX = 'CE'
    TEMPORARY_EX = 'TE'
    # TODO нахера тут эти константы?

    EXPENSEN_CHOISE = [
        (CONSTANT_EX, 'Постояный расход'),
        (TEMPORARY_EX, 'Временный раход'),
    ]

    title = models.CharField(max_length=255)
    expenses = models.CharField(max_length=100, choices=EXPENSEN_CHOISE, default=CONSTANT_EX)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f'Expenses from {self.expenses}: {self.amount}'

