import random
# совсем простой вариант игры

player = 'x'
ai = 'o'


def foolproof(inputed):  # защита от дурака
    return True if str(inputed).isdigit() and 1 <= int(inputed) <= 9 else False


def is_end(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if c1 == c2 == c3 or c1 == c4 == c7 or c1 == c5 == c9:
        return c1
    elif c4 == c5 == c6 or c2 == c5 == c8 or c3 == c5 == c7:
        return c5
    elif c7 == c8 == c9 or c3 == c6 == c9:
        return c9


def final(c1, c2, c3, c4, c5, c6, c7, c8, c9, player, ai):
    if is_end(c1, c2, c3, c4, c5, c6, c7, c8, c9) == player:
        return player
    elif is_end(c1, c2, c3, c4, c5, c6, c7, c8, c9) == ai:
        return ai


def ai_move(c1, c2, c3, c4, c5, c6, c7, c8, c9, player, ai):
    # логика атаки
    if c1 == '_' and (c2 == c3 == ai or c4 == c7 == ai or c5 == c9 == ai):
        return 1
    elif c2 == '_' and (c1 == c3 == player or c5 == c8 == player):
        return 2
    elif c3 == '_' and (c1 == c2 == player or c9 == c6 == player or c7 == c5 == player):
        return 3
    elif c4 == '_' and (c1 == c7 == player or c5 == c6 == player):
        return 4
    elif c5 == '_' and (c1 == c9 == player or c3 == c7 == player or c2 == c8 == player or c4 == c6 == player):
        return 5
    elif c6 == '_' and (c4 == c5 == player or c3 == c9 == player):
        return 6
    elif c7 == '_' and (c1 == c4 == player or c8 == c9 == player or c3 == c5 == player):
        return 7
    elif c8 == '_' and (c7 == c9 == player or c2 == c5 == player):
        return 8
    elif c9 == '_' and (c7 == c8 == player or c1 == c5 == player or c3 == c6 == player):
        return 9
    # логика защиты
    elif c1 != ai and (c2 == c3 == player or c4 == c7 == player or c5 == c9 == player):
        return 1
    elif c2 != ai and (c1 == c3 == player or c5 == c8 == player):
        return 2
    elif c3 != ai and (c1 == c2 == player or c9 == c6 == player or c7 == c5 == player):
        return 3
    elif c4 != ai and (c1 == c7 == player or c5 == c6 == player):
        return 4
    elif c5 != ai and (c1 == c9 == player or c3 == c7 == player or c2 == c8 == player or c4 == c6 == player):
        return 5
    elif c6 != ai and (c4 == c5 == player or c3 == c9 == player):
        return 6
    elif c7 != ai and (c1 == c4 == player or c8 == c9 == player or c3 == c5 == player):
        return 7
    elif c8 != ai and (c7 == c9 == player or c2 == c5 == player):
        return 8
    elif c9 != ai and (c7 == c8 == player or c1 == c5 == player or c3 == c6 == player):
        return 9
    else:
        s = random.randint(1, 9)
        return s


playdeck = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
c1 = playdeck[0]
c2 = playdeck[1]
c3 = playdeck[2]
c4 = playdeck[3]
c5 = playdeck[4]
c6 = playdeck[5]
c7 = playdeck[6]
c8 = playdeck[7]
c9 = playdeck[8]

while not final(c1, c2, c3, c4, c5, c6, c7, c8, c9, player, ai) and '_' in playdeck:
    # showdown
    print(c1, c2, c3)
    print(c4, c5, c6)
    print(c7, c8, c9)

    print(
        'Input the number to make the move:',
        '1 2 3',
        '4 5 6',
        '7 8 9',
        sep='\n'
    )
    m = input()
    if foolproof(m) and playdeck[int(m)-1] == '_':
        playdeck[int(m)-1] = player
        c1 = playdeck[0]
        c2 = playdeck[1]
        c3 = playdeck[2]
        c4 = playdeck[3]
        c5 = playdeck[4]
        c6 = playdeck[5]
        c7 = playdeck[6]
        c8 = playdeck[7]
        c9 = playdeck[8]
    else:
        print('Wrong selection. Try again')
        continue

    m = ai_move(c1, c2, c3, c4, c5, c6, c7, c8, c9, player, ai)
    if foolproof(m) and playdeck[int(m) - 1] == '_':
        playdeck[int(m) - 1] = ai
        c1 = playdeck[0]
        c2 = playdeck[1]
        c3 = playdeck[2]
        c4 = playdeck[3]
        c5 = playdeck[4]
        c6 = playdeck[5]
        c7 = playdeck[6]
        c8 = playdeck[7]
        c9 = playdeck[8]

if '_' in playdeck:
    print(c1, c2, c3)
    print(c4, c5, c6)
    print(c7, c8, c9)
    winner = final(c1, c2, c3, c4, c5, c6, c7, c8, c9, player, ai)
    print('Who plays "', winner, '" won')
else:
    print(c1, c2, c3)
    print(c4, c5, c6)
    print(c7, c8, c9)
    print('Draw')