# Задача:
# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое
# исло n — столько элементов последовательности должна отобразить программа. На выходе ожидается
# последовательность чисел, записанных через пробел в одну строку.
#
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

a = int(input())
i = 0
x = 0
name = []
while i <= a:
    if a == 1:
        print(a)
        break
    if len(name) >= a + 1:
        name3 = name[:a]
        for i in name3:
            print(i + ' ', end='')
        break
    elif i >= 0:
        x += 1
        i += 1
        name2 = [str(x)] * i
        name += name2