import random

def print_frame():
    print('Ход №', len(wrong) + len(correct) + 1)
    for x in secret:
        if x in correct:
            print(x, end='')
        else:
            print('-', end='')
    print()
    print('Ошибки:', *wrong)
    print(frames[len(wrong)])

def get_user_input():
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    while True:
        user_input = input('Ваш ход: ').lower()
        if len(user_input) > 1:
            print('Нужно вводить по одной букве. Повторите ввод.')
            continue
        if user_input not in alf:
            print('Слово состоит только из русских букв. Повторите ввод.')
            continue
        if user_input in wrong or user_input in correct:
            print('Такая буква уже называлась. Повторите ввод.')
            continue
        return user_input

def check_win():
    for c in secret:
        if c not in correct:
            return False
    return True

frames = [
'''
--------
  |   ||
      ||
      ||
      ||
      ||
--------
''','''
--------
  |   ||
  o   ||
      ||
      ||
      ||
--------
''','''
--------
  |   ||
  o   ||
  0   ||
      ||
      ||
--------
''','''
--------
  |   ||
  o   ||
 /0   ||
      ||
      ||
--------
''','''
--------
  |   ||
  o   ||
 /0\\  ||
      ||
      ||
--------
''','''
--------
  |   ||
  o   ||
 /0\\  ||
 /    ||
      ||
--------
''','''
--------
  |   ||
  o   ||
 /0\\  ||
 / \\  ||
      ||
--------
'''
]

fin = open('words.txt', 'r')
words = fin.read().splitlines()
fin.close()

secret = random.choice(words)

wrong = []
correct = []

print('Компьютер загадал слово. Вам нужно его отгадать, называя буквы.')

game_on = True
while game_on:
    print_frame()
    user_input = get_user_input()
    if user_input in secret:
        correct.append(user_input)
    else:
        wrong.append(user_input)
    if len(wrong) == len(frames) - 1:
        print('Вы проиграли')
        game_on = False
    if check_win():
        print('Вы победили! Слово отгадано.')
        game_on = False
    