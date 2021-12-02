
import random

player = 'x'
ai = 'o'
hello = "Hello there! \n Let's play a tic-tac-toe game! \n The order is to make 3 symbols in a row or diagonal and interfere your opponent to do the same. \n Move by move you'll fill a table 3*3 by symbols, usually 'x' and 'o'. You can write a symbol only in free cell. \n So, let's start!"

def get_user_move(): 
    """Возвращает номер клетки с ходом игрока. Или продолжает запрашивать ход
    """
    while True:
        print(
        'Enter the number of cell to make the move:',
        '1 2 3',
        '4 5 6',
        '7 8 9',
        sep='\n'
    )
        player_cell = input()
        if str(player_cell).isdigit() and int(player_cell) in range(10) and playdeck[int(player_cell) - 1] == 0:
            return int(player_cell)
        print('Wrong. Please try again.')
        print()

def get_ai_move(deck):
    """ Возвращает номер клетки с ходом компьютера, исходя из ситуации
    """
    for i in range(1, 8, 3):
        if deck[i+1] == deck[i+2] == player and deck[i] == 0:
            return i
    for j in range(2, 9, 3):
        if deck[i-1] == deck[i+1] == player and deck[j] == 0:
            return j
    for k in range(3, 9, 3):
        if deck[k-2] == deck[k-1] == player and deck[k] == 0:
            return k
    for a in range(1, 4):
        if deck[a] == deck[a+3] == player and deck[a] == 0:
            return a
    for b in range(4, 7):
        if deck[b-3] == deck[b+3] == player and deck[b] == 0:
            return b
    for c in range(7, 10):
        if deck[c-6] == deck[c-3] == player and deck[c] == 0:
            return c
    if deck[5] == deck[9] and deck[1] == 0:
        return 1
    if deck[1] == deck[5] and deck[9] == 0:
        return 9
    if deck[3] == deck[5] and deck[7] == 0:
        return 7
    if deck[7] == deck[5] and deck[3] == 0:
        return 3
    if (deck[1] == deck[9] or deck[3] == deck[7]) and deck[5] == 0:
        return 5

def winner(deck):
    """Возвращает символ победителя. 
    """
    for i in range(1, 8, 3):
        if deck[i] == deck[i+1] == deck[i+2] and deck[i] != 0:
            return deck[i]
    for j in range(1, 4, 3):
        if deck[j] == deck[j+3] == deck[j+6] and deck[j] != 0:
            return deck[j]
    if deck[1] == deck[5] == deck[9] or deck[3] == deck[5] == deck[7]:
        return deck[5]

def is_end(deck):
    """Анализирует доску и возвращает True, если игра закончена. Иначе False 
    """
    if 0 not in deck:
        return True
    for i in range(1, 8, 3):
        if deck[i] == deck[i+1] == deck[i+2] and deck[i] != 0:
            return True
    for j in range(1, 4, 3):
        if deck[j] == deck[j+3] == deck[j+6] and deck[j] != 0:
            return True
    if deck[1] == deck[5] == deck[9] or deck[3] == deck[5] == deck[7]:
        return True
    return False

def game():
    print(hello)
    playdeck = [0, 0, 0, 0, 0, 0, 0, 0, 0]    
    while True:
        user_move = get_user_move() - 1
        playdeck[user_move] = player
        is_end(playdeck)
        ai_move = get_ai_move(playdeck) - 1
        playdeck[ai_move] = ai
        is_end(playdeck)
    print('And who plays', winner(playdeck), ' won')
    # print who wins
    # ask try again
game()

# TODO algorhytm
    
   

# while not end_of_game and 0 in playdeck:
#     # showdown
#     print(playdeck[0], playdeck[1], playdeck[2])
#     print(playdeck[3], playdeck[4], playdeck[5])
#     print(playdeck[6], playdeck[7], playdeck[8])

