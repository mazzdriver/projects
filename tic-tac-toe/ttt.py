from random import choice

player = 'x'
ai = 'o'
hello = "Hello there! \n Let's play a tic-tac-toe game! \n The order is to make 3 symbols in a row or diagonal and interfere your opponent to do the same. \n Move by move you'll fill a table 3*3 by symbols, usually 'x' and 'o'. You can write a symbol only in free cell. \n So, let's start!"

def get_user_move(moves): 
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
        if str(player_cell).isdigit() and int(player_cell) in moves:
            return int(player_cell)
        print('Wrong. Please try again.')
        print()

def get_ai_move(deck):
    """ Возвращает номер клетки с ходом компьютера, исходя из ситуации
    """
    ongoing = []
    for i in range(0, 8, 3):
        if deck[i+1] == deck[i+2] == player and deck[i] == 0:
            ongoing.append(i)
    for j in range(1, 9, 3):
        if deck[i-1] == deck[i+1] == player and deck[j] == 0:
            ongoing.append(j)
    for k in range(2, 9, 3):
        if deck[k-2] == deck[k-1] == player and deck[k] == 0:
            ongoing.append(k)
    for a in range(0, 3):
        if deck[a] == deck[a+3] == player and deck[a] == 0:
            ongoing.append(a)
    for b in range(3, 6):
        if deck[b-3] == deck[b+3] == player and deck[b] == 0:
            ongoing.append(b)
    for c in range(6, 9):
        if deck[c-6] == deck[c-3] == player and deck[c] == 0:
            ongoing.append(c)
    if deck[4] == deck[8] and deck[0] == 0:
        ongoing.append(1)
    if deck[0] == deck[4] and deck[8] == 0:
        ongoing.append(9)
    if deck[2] == deck[5] and deck[6] == 0:
        ongoing.append(7)
    if deck[6] == deck[5] and deck[2] == 0:
        ongoing.append(3)
    if (deck[0] == deck[8] or deck[2] == deck[6]) and deck[4] == 0:
        ongoing.append(5)
    while True:
        out = choice(ongoing) 
        if out in legal_moves:
            return out
    

def winner(deck):
    """Возвращает символ победителя. 
    """
    for i in range(0, 8, 3):
        if deck[i] == deck[i+1] == deck[i+2] and deck[i] != 0:
            return deck[i]
    for j in range(0, 3):
        if deck[j] == deck[j+3] == deck[j+6] and deck[j] != 0:
            return deck[j]
    if deck[0] == deck[4] == deck[8] or deck[2] == deck[4] == deck[6]:
        return deck[4]

def is_end(deck):
    """Анализирует доску и возвращает True, если игра закончена. Иначе False 
    """
    if 0 not in deck:
        return True
    for i in range(0, 8, 3):
        if deck[i] != 0 and deck[i] == deck[i+1] == deck[i+2]:
            return True
    for j in range(0, 4):
        if deck[j] != 0 and deck[j] == deck[j+3] == deck[j+6]:
            return True
    if deck[0] == deck[4] == deck[8] or deck[2] == deck[4] == deck[6]:
        return True
    return False

def game():
    print(hello)
    playdeck = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    legal_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    while True:
        print(playdeck)
        user_move = get_user_move(legal_moves) - 1
        playdeck[user_move] = player
        legal_moves.remove(user_move+1)
        if is_end(playdeck):
            break
        ai_move = get_ai_move(playdeck) - 1
        playdeck[ai_move] = ai
        legal_moves.remove(ai_move+1)
        if is_end(playdeck):
            break
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

