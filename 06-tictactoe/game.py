import random

def make_board() -> list:
    '''Создает игровое поле'''
    return [' '] * 10

def print_board(board: list) -> None:
    '''Выводит на экран игровое поле'''
    print(board[7], '|', board[8], '|', board[9])
    print('-' * 9)
    print(board[4], '|', board[5], '|', board[6])
    print('-' * 9)
    print(board[1], '|', board[2], '|', board[3])

def get_user_move() -> int:
    '''Получает ход игрока с проверкой корректности'''
    while True:
        x = input('Ваш ход в клетку (1-9): ')
        if not x.isdigit():
            print('Нужно ввести число! Повторите попытку.')
            continue
        x = int(x)
        if x > 9 or x < 1:
            print('Число должно быть в пределах доски (1-9)')
            continue
        if board[x] != ' ':
            print('Клетка уже занята. Попробуйте другую.')
            continue
        return x

def get_computer_move() -> int:
    '''Получает ход компьютера'''
    free = []
    for i in range(1, 10):
        if board[i] == ' ':
            free.append(i)
    return random.choice(free)

def check_win(board: list, tile: str) -> bool:
    '''Проверяет условие победы'''

def check_draw(board: list) -> bool:
    '''Проверяет ничью'''
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True


board = make_board()
board[8] = 'X'
board[6] = 'O'
print_board(board)