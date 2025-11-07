import time, random

print('ПЕЩЕРА ДРАКОНА')
time.sleep(1)
print('Вы спускаетесь в пещеру Дракона. Перед вами две двери.')
time.sleep(1)
print('За одной из них находится сундук с сокровищами, за другой - голодный дракон.')
time.sleep(2)
print('В какую дверь вы войдете (1 или 2)?')
userchoice = int(input())
computerchoice = random.randint(1, 2)
time.sleep(1)
print('Вы выбираете дверь', userchoice)
time.sleep(2)
print('Ключ со скрипом поворачивается в замке...')
time.sleep(3)
print('Во тьме подземелья трудно понять, что за ней...')
time.sleep(3)
print('Наконец, вы с трудом различаете...')
time.sleep(3)
if userchoice == computerchoice:
    print('Сундук с золотыми монетами. Поздравляем! Вы нашли сокровище!')
else:
    print('Голодного огнедышащего дракона. Вы проиграли.')