# Task by YADRO
# Проверить валидность расстановки скобочек в выражении.
# Скобки могут быть всех трех видов - ()[]{}.
# На вход программа или функция должна принимать строку, а на выходе ответить правильно ли расставлены скобочки в ней.
# Те есть открывающиеся скобочки корректно закрываются скобочкой того же вида.

# Например:

# "([])" - true
# "{[(]}"- false


def check_correct_spelling(string: str) -> bool:
    open_symbols = ('(', '[', '{')
    closed_symbols = (')', ']', '}')
    data = []
    for i in string:
        if i in open_symbols:
            data.append(i)
        if i in closed_symbols:
            if len(data) == 0:
                return False
            index = closed_symbols.index(i)
            open_symbol = open_symbols[index]
            if data[-1] == open_symbol:
                data = data[:-1]
            else:
                return False
    return not data


check_true = '([])'
check_false = '{[(]}"'

print(check_correct_spelling(check_true))
print(check_correct_spelling(check_false))

