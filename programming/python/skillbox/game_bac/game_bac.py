from game_bac_server import make_number, check_number, game_over
from termcolor import cprint, colored


cprint('Игра «Быки и коровы»', color='red')
cprint('Компьютер зкадал четырехзначное число, попробуй его отгадать', color='yellow')

make_number()
counter = 0

while True:
    user_push = input(colored('Введите число: ', color='blue'))
    cprint(check_number(user_push), color='white')
    counter += 1
    if game_over():
        print()
        cprint('Поздравляю, вы угадали загаданное число!', color='magenta')
        cprint('Ваше количество ходов - {}'.format(counter), color='blue')
        print()
        print('Хотите с играть еще раз?')
        cprint('Y - да, N - нет', color='cyan')
        if input() == 'Y':
            make_number()
            cprint('Компьютер зкадал новое четырехзначное число, удачи', color='yellow')
            continue
        else:
            cprint('Это была игра «Быки и коровы»! До новых встреч!', color='yellow')
        break

