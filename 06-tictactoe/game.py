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
    return board[1] == board[2] == board[3] == tile or \
       board[4] == board[5] == board[6] == tile or \
       board[7] == board[8] == board[9] == tile or \
       board[1] == board[4] == board[7] == tile or \
       board[2] == board[5] == board[8] == tile or \
       board[3] == board[6] == board[9] == tile or \
       board[1] == board[5] == board[9] == tile or \
       board[3] == board[5] == board[7] == tile

def check_draw(board: list) -> bool:
    '''Проверяет ничью'''
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True

print('Крестики-нолики')
print('Цель игры - поставить три фишки в ряд по горизонтали, вертикали или диагонали.')
print('Используйте цифровую клавиатуру, чтобы выбрать клетку для своего хода.')

tiles = ['X', 'O']
random.shuffle(tiles)
user_tile, computer_tile = tiles
print(f'Вы играете за {user_tile}. Поменять (y/n)? Нажмите Enter, чтобы оставить как есть.')
if input().lower().startswith('y'):
    user_tile, computer_tile = computer_tile, user_tile
    print(f'Теперь вы играете за {user_tile}.')
turn = random.choice(['компьютер', 'человек'])
print(f'Первым ходит {turn}.')

board = make_board()
game_on = True
while game_on:
    if turn == 'человек':
        print('Ход человека')
        print_board(board)
        move = get_user_move()
        board[move] = user_tile
        if check_win(board, user_tile):
            print('Вы победили!')
            game_on = False
        turn = 'компьютер'
    else:
        print('Ход компьютера')
        print_board(board)
        move = get_computer_move()
        board[move] = computer_tile
        if check_win(board, computer_tile):
            print('Победил компьютер')
            game_on = False
        turn = 'человек'
    if check_draw(board):
        print('Ничья.')
        game_on = False