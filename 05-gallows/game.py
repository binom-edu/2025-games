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
    user_input = input()
    if user_input in secret:
        correct.append(user_input)
    else:
        wrong.append(user_input)