import random
secret = random.randint(1, 100)
print('Компьютер загадал число от 1 до 100. Попробуйте его отгадать.')
game_on = True
attempt = 1
while game_on:
    userchoice = input(f'Попытка {attempt}. Введите ваше число: ')
    if userchoice.isdigit():
        userchoice = int(userchoice)
    else:
        print('Требуется число. Повторите ввод.')
        continue
    if userchoice == secret:
        print('Поздравляем! Вы отгадали число.')
        game_on = False
    elif userchoice > secret:
        print('Загаданное число меньше.')
    else:
        print('Загаданное число больше')
    attempt = attempt + 1
    if attempt == 9:
        print('Попытки закончились.')
        game_on = False

print(f'Затрачено попыток: {attempt}')