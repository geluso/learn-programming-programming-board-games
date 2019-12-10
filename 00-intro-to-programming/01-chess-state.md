## Modelling Chess
So, what would you need for Cheese? Sorry, Chess.

First of all: there are SO MANY ways to represent a game. There's not going to
be any one perfect way to capture the state of a Chess game, or any other game,
or any other program. Refer to the short topic in the Personal Philosophies
section, [Rightness vs Ramifications]().

Here's one way to store all the data of a Chess game. You can use one String to
make a big grid of the whole board and manually place a letter at the locations
for each piece. You can even represent "black" and "white" using different
uppercase and lowercase letters!

```
RNBKQBNR
PPPPPPPP
........
........
........
........
rnbkqbnr
pppppppp
```

It's totally possible to store a game like this. Actually it's a very good way
to begin serializing a game to save it (see [Serialization]()).

Another way to store the data would be to recreate the 8x8 Chess grid using a
two-dimensional array, an array of arrays.

```
[
  [
    {color: 'white', type: 'rook'}, {color: 'white', type: 'knight'}, 
    {color: 'white', type: 'bishop'}, {color: 'white', type: 'king'}, 
    {color: 'white', type: 'queen'}, {color: 'white', type: 'bishop'}, 
    {color: 'white', type: 'knight'}, {color: 'white', type: 'rook'}
  ],
  [
    {color: 'white', type: 'pawn'}, {color: 'white', type: 'pawn'}, 
    {color: 'white', type: 'pawn'}, {color: 'white', type: 'pawn'}, 
    {color: 'white', type: 'pawn'}, {color: 'white', type: 'pawn'}, 
    {color: 'white', type: 'pawn'}, {color: 'white', type: 'pawn'}
  ],
  [null, null, null, null, null, null, null, null],
  [null, null, null, null, null, null, null, null],
  [null, null, null, null, null, null, null, null],
  [null, null, null, null, null, null, null, null],
  [
    {color: 'black', type: 'pawn'}, {color: 'black', type: 'pawn'}, 
    {color: 'black', type: 'pawn'}, {color: 'black', type: 'pawn'}, 
    {color: 'black', type: 'pawn'}, {color: 'black', type: 'pawn'}, 
    {color: 'black', type: 'pawn'}, {color: 'black', type: 'pawn'}
  ],
  [
    {color: 'black', type: 'rook'}, {color: 'black', type: 'knight'}, 
    {color: 'black', type: 'bishop'}, {color: 'black', type: 'king'}, 
    {color: 'black', type: 'queen'}, {color: 'black', type: 'bishop'}, 
    {color: 'black', type: 'knight'}, {color: 'black', type: 'rook'}
  ],
]
```

