
import random
# совсем простой вариант игры

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


def ai_move():
    """ Возвращает номер клетки с ходом компьютера, исходя из ситуации
    """
    pass
# TODO logic
    # for i in range(10):
        # if playdeck[i] == 0 and (c2 == c3 == ai or c4 == c7 == ai or c5 == c9 == ai):
    #     return 1
    # elif c2 == '_' and (c1 == c3 == player or c5 == c8 == player):
    #     return 2
    # elif c3 == '_' and (c1 == c2 == player or c9 == c6 == player or c7 == c5 == player):
    #     return 3
    # elif c4 == '_' and (c1 == c7 == player or c5 == c6 == player):
    #     return 4
    # elif c5 == '_' and (c1 == c9 == player or c3 == c7 == player or c2 == c8 == player or c4 == c6 == player):
    #     return 5
    # elif c6 == '_' and (c4 == c5 == player or c3 == c9 == player):
    #     return 6
    # elif c7 == '_' and (c1 == c4 == player or c8 == c9 == player or c3 == c5 == player):
    #     return 7
    # elif c8 == '_' and (c7 == c9 == player or c2 == c5 == player):
    #     return 8
    # elif c9 == '_' and (c7 == c8 == player or c1 == c5 == player or c3 == c6 == player):
    #     return 9
    # # логика защиты
    # elif c1 != ai and (c2 == c3 == player or c4 == c7 == player or c5 == c9 == player):
    #     return 1
    # elif c2 != ai and (c1 == c3 == player or c5 == c8 == player):
    #     return 2
    # elif c3 != ai and (c1 == c2 == player or c9 == c6 == player or c7 == c5 == player):
    #     return 3
    # elif c4 != ai and (c1 == c7 == player or c5 == c6 == player):
    #     return 4
    # elif c5 != ai and (c1 == c9 == player or c3 == c7 == player or c2 == c8 == player or c4 == c6 == player):
    #     return 5
    # elif c6 != ai and (c4 == c5 == player or c3 == c9 == player):
    #     return 6
    # elif c7 != ai and (c1 == c4 == player or c8 == c9 == player or c3 == c5 == player):
    #     return 7
    # elif c8 != ai and (c7 == c9 == player or c2 == c5 == player):
    #     return 8
    # elif c9 != ai and (c7 == c8 == player or c1 == c5 == player or c3 == c6 == player):
    #     return 9
    # else:
    #     s = random.randint(1, 9)      
    #     return s



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
    pass
    print(hello)
    while True:
        playdeck = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        user_move = get_user_move()
        is_end(playdeck)
        ai_move()
        is_end(playdeck)
    winner(playdeck)
    # print who wins
    # ask try again

# TODO algorhytm
    
   

# while not end_of_game and 0 in playdeck:
#     # showdown
#     print(playdeck[0], playdeck[1], playdeck[2])
#     print(playdeck[3], playdeck[4], playdeck[5])
#     print(playdeck[6], playdeck[7], playdeck[8])

