from random import randint


secret_number = ''
bulls_cows = {'Быки': 0, 'Коровы': 0}


def make_number():
    global secret_number
    secret_number = ''
    while len(secret_number) < 4:
        number = str(randint(1, 9))
        if number in secret_number:
            continue
        else:
            secret_number += str(number)
    return secret_number


def check_number(user_push):
    global bulls_cows
    bulls_cows = {'Быки': 0, 'Коровы': 0}
    counter = 0
    for i in str(user_push):
        if i == secret_number[counter]:
            bulls_cows['Быки'] += 1
            counter += 1
            continue
        else:
            if i in secret_number:
                bulls_cows['Коровы'] += 1
        counter += 1
    return list(bulls_cows.items())


def game_over():
    return bulls_cows['Быки'] == 4