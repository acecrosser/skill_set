# Задача:
# Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,
# которая выводит все позиции, на которых встречается число x в переданном списке lst.
# Позиции нумеруются с нуля, если число x не встречается в списке,
# вывести строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

lst = input().split()
x = input()

l = 0

for i in lst:
    if lst.count(x) > 0:
        if x != i:
            l += 1
        elif x == i:
            print(l, ' ', end='')
            l += 1
    elif lst.count(x) == 0:
        print('Отсутствует')
        break