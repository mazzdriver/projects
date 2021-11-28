
import random
# совсем простой вариант игры

player = 'x'
ai = 'o'
playdeck = [0, 0, 0, 0, 0, 0, 0, 0, 0]



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
        if str(player_cell).isdigit() and 1 <= int(player_cell) <= 9 and playdeck[int(player_cell)] == 0:
            return int(player_cell)
        print('Wrong. Please try again.')
        print()

def ai_move():
    """ Возвращает ход компьютера, исходя из ситуации
    """
    pass
    # c1, c2, c3, c4, c5, c6, c7, c8, c9, player, ai):
    # # логика атаки
    # if c1 == '_' and (c2 == c3 == ai or c4 == c7 == ai or c5 == c9 == ai):
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



def is_win():
    """Анализирует возможность ходить далее. Возвращает символ победителя. 
    """
    pass
    # if c1 == c2 == c3 or c1 == c4 == c7 or c1 == c5 == c9:
    #     return c1
    # elif c4 == c5 == c6 or c2 == c5 == c8 or c3 == c5 == c7:
    #     return c5
    # elif c7 == c8 == c9 or c3 == c6 == c9:
    #     return c9


def final():
    """
    """
    pass
# (c1, c2, c3, c4, c5, c6, c7, c8, c9, player, ai):
#     if is_end(c1, c2, c3, c4, c5, c6, c7, c8, c9) == player:
#         return player
#     elif is_end(c1, c2, c3, c4, c5, c6, c7, c8, c9) == ai:
#         return ai


def game():
    pass
    
    # - приветствие
    # - запрос хода
    # - проверка хода
    # - изменение поля
    # - ход компьютера
    # - изменение поля
    # - запрос хода



# while not end_of_game and 0 in playdeck:
#     # showdown
#     print(playdeck[0], playdeck[1], playdeck[2])
#     print(playdeck[3], playdeck[4], playdeck[5])
#     print(playdeck[6], playdeck[7], playdeck[8])

