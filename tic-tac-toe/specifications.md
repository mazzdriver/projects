# Specifications

##### Tic-tac-toe game

Step by step, move by move a game goes to the end.

Goal of a game is to fill a row or diagonal with your symbols.

Field contents 9 cells in the table 3*3. So, you need to make 3 crosses or 3 circles in one line. You also can interfere your opponent.

```
----------- 
 x |   | x
-----------
 o | x |
-----------
 o | o | x
-----------
```

In this case crosses won: 3 crosses in diagonal.

##### Logic of the game:
   
1. Write a deck for game. 
2. Get actual status of playdeck.
3. Let the player make a move by placing the symbol in clear cell.

Note that move must match the next specific:
- entered text should be a integer (int)
- move must be in range
- selected cell must be free

##### Plan

- function about inputting
- function about AI move
- function about final analysis
- function about legal move
- field
- symbol
