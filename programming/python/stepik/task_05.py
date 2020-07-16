# Задача:
# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# Sample Input:
# a3b4c2e10b1
# Sample Output:
# aaabbbbcceeeeeeeeeeb

with open('file.txt') as file:
    s1 = file.readline().strip()
    integ = []
    string = []
    i = 0
    while i < len(s1):
        s_int = ''
        a = s1[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s1[i]
            else:
                break
        string += a
        i += 1
        if s_int != '':
            integ.append(int(s_int))

    summa = ''
    i = 0
    b = 0
    for i in integ:
        summa += string[b] * i
        b += 1
        i += 1

file = open('file_result.txt', 'w')
file.write(summa)
file.close()

