import random


def make_secret(n: int) -> str:
    '''
    Создает новое число длины n без повторяющихся цифр
    
    :param n: требуемое количество цифр в числе
    :type n: int
    :return: число в строковом представлении
    :rtype: str
    '''

    s = random.choice('123456789')
    while len(s) < n:
        c = random.choice('0123456789')
        if c not in s:
            s += c
    return s

def get_user_input(n: int) -> str:
    '''
    Получает ход игрока с проверкой корректности

    :param n: требуемое количество цифр в числе
    :type n: int    
    :return: число заданной длины
    :rtype: str
    '''
    while True:
        s = input(f'Введите {n}-значное число: ')
        if len(s) != n:
            print(f'Должно быть ровно {n} знаков.')
            continue
        if not s.isdigit():
            print('Ввод должен состоять только из цифр.')
            continue
        return s
    
def check(secret: str, guess: str) -> dict:
    '''
    Проверяет догадку и подсчитывает быков и коров в строке guess.

    :param secret: загаданное компьютером число
    :type secret: str
    :param guess: догадка пользователя
    :type guess: str
    :return: словарь, в котором bulls - количество быков, cows - количество коров
    :rtype: dict
    '''
    res = {'bulls': 0, 'cows': 0}
    for i in range(n):
        if guess[i] == secret[i]:
            res['bulls'] += 1
        elif guess[i] in secret:
            res['cows'] += 1
    return res

n = 3
secret = make_secret(n)
game_on = True
while game_on:
    move = get_user_input(n)
    res = check(secret, move)
    print('Результат проверки: быков -', res['bulls'], 'коров -', res['cows'])
    if res['bulls'] == n:
        print('Вы выиграли!')
        game_on = False