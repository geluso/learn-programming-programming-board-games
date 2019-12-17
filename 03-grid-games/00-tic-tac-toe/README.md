# Tic Tac Toe
Write a program that allows two players to play a game of Tic Tac Toe.

Here's what we'll need for the program:

* A way to represent the board
* A way to display the board
* Keep track of who's turn it is
* Allow players to make moves
* Prevent players from making impossible moves
* Detect if a player wins

Most of these items will be accomplished without much trouble. Our biggest
challenge will be writing some code to detect when the game is won (or over).
Let's build up the game then see what it takes to detect end-game conditions.

## Two-Dimensional Array Coordinates
Let's start with the board representation. A two-dimensional array is a great
choice for this grid game. Here's a 3x3 grid filled with `null` values to
represent an empty board. Let's practice accessing different spots on the
board to make sure we've got our coordinates all figured out.

```
board = [
  [null, null, null],
  [null, null, null],
  [null, null, null],
]
```

We're saving the entire two-dimensional grid in to a variable called `board`.
The board has three rows going from top to bottom, and three columns going
from left to right.

If we want to access the top-left corner of the board we would access
`board[0][0]` because it's in the first row, in the first column. Remember
that the grid is an array of arrays. That is to say, the `board` variable
itself refers to one array. That array contains three things. Each of those
things is an array itself. Each of the inner arrays has three empty spots.

* The top left corner is at index `board[0][0]`
* The middle spot is at index `board[1][1]`
* The bottom left corner is at index `board[2][0]`
* The middle bottom spot is at index `board[2][1]`
* The bottom right corner is at index `board[2][2]`

If you come from a background dealing with (x,y) coordinates with lines and
graphs like in a math class you might notice something odd here. In math
classes when we plot lines we usually draw a graph with the origin `(0,0)` in
the bottom left, and two: one for `x` extending to the right, and one for `y`
extending up.

If we plotted each `board[row][column]` index as points on a graph we would
see something different than we're used to seeing in math. In math graphs the
`y` coordinates start at zero in the bottom left and their values increase as
they go up. The way we access our array the row `"y"` coordinates start at
`0` at the top and they increase as they go down. This is a common thing in
computer graphics. Often in computer graphics the top of the screen is where
the zero value for y-coordinates start, and the y-coordinates increase as you
move from the top of the screen toward the bottom.

Since I'm personally used to y-coordinates increasing as they go up I strive
to refer to array indexes with the words "row" and "column," especially in
strictly grid-like structures. It makes it easier for me to reason about
where things are located.

## Game Engine
Here's a simplified version of how the main program will use this class.
Notice how the main program primarily uses the methods `isGameOver`, and
`makeMove`.

```js
game = new TicTacToeGame()
while (!game.isGameOver()) {
  row, col = promptPlayer(game)
  game.makeMove(row, col)
  displayBoard(game)
}
displayWinner(game)
```

Some complexity of this program has been abstracted away with the methods
display methods `displayBoard` and `displayWinner`. You can assume those
methods would interact with more `TicTacToeGame` methods like
`getCurrentPlayer()` and `getWinner()`.

Here's an outline of the whole `TicTacToeGame` class:

```js
class TicTacToeGame {
  winner = null
  isGameOver = false

  turn = 0
  players = ['X', 'O']

  board = [
    [null, null, null],
    [null, null, null],
    [null, null, null]
  ]

  resetGame() {}
  makeMove(row, col) {}

  getBoard() {}
  getCurrentPlayer() {}

  isGameOver() {}
  getWinner() {}

  isValidMovie(row, col) {}
  checkGameOver() {}
}
```

It has some state to keep track of if the game is over and who won. It has a
variable `turn` to keep track of what turn it is. Knowing what number turn it
is will help us determine which player is making a move. The class will use
the `turn` number along with the `players` array with `"X"` and `"O"`
strings to keep track of the players.

The class has a reference to the two-dimensional array representing the board
and it has methods to manipulate all of these things together.

Notice that the class has some methods that we'll use with from outside the
class, and two methods that will only be used by the class internally. The
idea here is that our main program doesn't need access to every method in the
class. It will call methods like `isGameOver()` to see if the program should
continue running. It won't need to call methods like `isValidMove()` because 
`makeMove()` will call that method internally itself. Programming languages
often call the different between externally-used and internally-used methods
`public` and `private` methods.

Read more about [encapsulation]().

## Taking Turns
Here's a very common pattern while programming board games: having players
take turns! Here's the general pattern we'll follow:

* Have the current player attempt to make a move
* Double-check to make sure the move is legitimate
* Manipulate the state of the game as per the move
* Advance the state of the game to the next player

Keeping track of the current player is conveniently tracked using the array
of players, counting how many turns have occurred, and using the modulus
operator. Check out this little example first:

```js
// referring to a Star Trek TNG poker scene
// https://www.youtube.com/watch?v=XRE9HNUmdtA
players = ['Beverly', 'Riker', 'Geordie', 'Worf', 'Data']
turn = 0
while (turn < 42) {
  index = turn % players.length
  player = players[index]
  console.log('current player:', player)

  turn++
}
```

**Takeaway:** You can always use an integer, an array, and the modulus
operator to proceed through players's turns in an orderly fashion until a
game is over. When you take the turn number "modulo" the length of the array
you end up with a number sequence that cycles through indexes of the array.

Here's an example using this modulus trick in a two player game, and a five
player game. No matter how many players are in the game this trick will
always work.

(Well, technically there's one specific thing that could cause this trick to
hiccup. Read more about [Integer Overflow](). Practically it would only
happen if your game lasted many, many, many turns.)


| Turn | turn % 2    | Two Players | turn % 5    | Five Players |
| ---- | ----------- | ----------- | ----------- | ------------ |
| 0    | 0 % 2 == 0  | Alice       | 0 % 5 == 0  | Beverly      |
| 1    | 1 % 2 == 1  | Bob         | 1 % 5 == 1  | Riker        |
| 2    | 2 % 2 == 0  | Alice       | 2 % 5 == 2  | Geordie      |
| 3    | 3 % 2 == 1  | Bob         | 3 % 5 == 3  | Worf         |
| 4    | 4 % 2 == 0  | Alice       | 4 % 5 == 4  | Data         |
| 5    | 5 % 2 == 1  | Bob         | 5 % 5 == 0  | Beverly      |
| 6    | 6 % 2 == 0  | Alice       | 6 % 5 == 1  | Riker        |
| 7    | 7 % 2 == 1  | Bob         | 7 % 5 == 2  | Geordie      |
| 8    | 8 % 2 == 0  | Alice       | 8 % 5 == 3  | Worf         |
| 9    | 9 % 2 == 1  | Bob         | 9 % 5 == 4  | Data         |
| 10   | 10 % 2 == 0 | Alice       | 10 % 5 == 0 | Beverly      |
| 11   | 11 % 2 == 1 | Bob         | 11 % 5 == 1 | Riker        |
| 12   | 12 % 2 == 0 | Alice       | 12 % 5 == 2 | Geordie      |
| 13   | 13 % 2 == 1 | Bob         | 13 % 5 == 3 | Worf         |


Here's code for taking a turn of Tic Tac Toe. We'll look more at the
`checkGameOver` next.

```js
getCurrentPlayer() {
  index = this.turn % this.players.length
  return this.players[index]
}

makeMove(row, col) {
  if (this.isValidMove(row, col)) {
    // mark the board with the current player ("X" or "O")
    this.board[row][col] = this.getCurrentPlayer()
    this.turn++

    // check to see if the move ended the game
    this.checkGameOver()
  }
}

isValidMove(row, col) {
  // make sure indexes are legitimate array indexes within the grid
  if (row < 0 || col < 0 || row >= 3 || col >= 3) {
    return false
  }

  // make sure the spot on the grid hasn't already been taken
  if (board[row][col] !== null) {
    return false
  }

  return true
}
```

## Checking For Game Over
OK, now we've got a class set up to represent the whole Tic Tac Toe game. The
class uses a two-dimensional array to represent the board. It's got methods
that allow players to make moves, it increments through play turns smoothly,
and makes sure players only play legitimate moves. Let's figure out when this
thing ends!

When does Tic Tac Toe end?

* A player wins when that player gets three in a row. Players tie when the
* board fills up without either player scoring three-in-a-row and with nowhere
  else to play.

I apologize for having explained end-game conditions for Tic Tac Toe. If
you've serisously never played Tic Tac Toe, welcome to the game!

The actual annoying part about checking for three-in-a-row is writing the
code to do it. Let's use what we know about for-loops and arrays to write
code that checks for wins. After we look at using for-loops to check for
these win conditions I want to show off one simpler approach too.

### Traversing Arrays
Three in a row can occur in three (or four?) different patterns.

1. From left to right across a row (on the top, middle, or bottom rows)
1. From top to bottom along a column (along the left, middle, or right columns)
1. From top-left to bottom-right in a diagonal
1. From bottom-left to top-right in a diagonal

The row and column patterns occur three times so it makes sense to write
for-loops to try to capture some of the redundancy.

```js
// check each row for three-in-a-row across
for (let row = 0; row < board.length; row++) {
  let isNotNull = board[row][0] !== null
  let threeInARow = board[row][0] === board[row][1] && board[row][1] === board[row][2]

  if (isNotNull && threeInARow) {
    return true
  }
}

// check each column for three-in-a-row down
for (let col = 0; col < 3; col++) {
  let isNotNull = board[0][col] !== null
  let threeInARow = board[0][col] === board[1][col] && board[1][col] === board[2][col]

  if (isNotNull && threeInARow) {
    return true
  }
}
```

Ah, but there's redundant logic inside the for-loops! It's annoying to have
to write the same code inside the two for-loops twice. We can write a function
to capture this logic.

Read more about [Reducing Redundant Redundancy]() and why it can be a great thing.

This function checks three spots on the board and returns `true` or `false`
if all the spots match each other, and they are not `null`.

```js
function checkThree(row1, col1, row2, col2, row3, col3) {
  let isNotNull = board[row1][col1] !== null
  let threeInARow = board[row1][col1] === board[row2][col2] && board[row2][col2] === board[row3][col3]

  if (isNotNull && threeInARow) {
    return true
  }
  return false
}
```

## False Optimization
An astute reader will notice that the `checkThree` function above can be
"optimized," specifically around condensing the if-statement that takes up
four whole lines.

```js
function checkThree(row1, col1, row2, col2, row3, col3) {
  let isNotNull = board[row1][col1] !== null
  let threeInARow = board[row1][col1] === board[row2][col2] && board[row2][col2] === board[row3][col3]
  return isNotNull && threeInARow
}
```

The astute reader will realize the code can be "optimized" even further.

```js
function checkThree(a,b,c,d,e,f) {
  return board[a][b] !== null && board[a][b] === board[c][d] && board[c][d] === board[e][f]
}
```

This reader is a dolt, a coward, they are missing the forest for the trees,
seeing a finger for the moon, and prioritizing having less lines-of-code over
striving for clarity, investigatibility, and maintainability. This is a false
optimization, a bad habit, and no one wants to talk to these people at
parties.

Basically squishing code together like this just makes things harder to
understand and much harder to debug and log and interact with in the future.

Spreading code out across multiple lines (especially the hard-coded `true`
and `false` individual return statements) make it easy to observe what path
your program takes if you watch it execute it line-by-line with a debugger.

Saving boolean values into variables like `isNotNull` and `threeInARow` is a
great way simply to describe what logic check your performing. The next
person that reads the code (especially future-you) can quickly see what
you're trying to determine just by the name of the variable. Good debuggers
will let you see the value of the variable too, so it's nice to be able to
pause the program and see the result of those logics.

You're probably going to extend the program in the future and rewrite this code anyway.
Breaking code across many variable and across many lines will give you more
"contact points" in the future. More places to "hook up wires" or "weld stuff
on."

Read more about [One-Liners Suck]()

And another one thing!! Tiny variable names are absolutely terrible. Imagine
searching through a code-base to see everywhere a variable, or a function is
called. If you named something `a` you're going to get a lot of useless
search results like "banana," "banana," "banana," "bandana," "bandana,"
"bandana," "let a = 78", "search," and so on.

### A Simpler Solution

```js
// check each row for three-in-a-row across
for (let row = 0; row < board.length; row++) {
  if (checkThree(row, 0, row, 1, row, 2)) {
    return true
  }
}

// check each column for three-in-a-row down
for (let col = 0; col < 3; col++) {
  if (checkThree(0, col, 1, col, 2, col)) {
    return true
  }
}

// check diaganols
// top-left to bottom-right
if (checkThree(0, 0, 1, 1, 2, 2)) {
  return true
}

// bottom-left to top-right
if (checkThree(2, 0, 1, 1, 0, 3)) {
  return true
}

return false
```

## A More Complex Simple Solution
OK, there's one more variation on this game that I personally like. Instead
of using the two for loops and checking for the diaganols all seperately
we'll store all our line information the same way. The two for loops for the
horizontal lines and the vertical lines are not that big of a win.

Hard-code an array listing each of the potential three-in-a-row lines with
the row/column information for each space in the line. Tic-Tac-Toe is a small
enough game that I think it's ok to get away with this.

We'll look at more complicated grid-assessments when we look at Connect Four in
the next game.

```js
function hasWinner() {
  const lines = [
    // horizontal lines 
    [0, 0, 0, 1, 0, 2],
    [1, 0, 1, 1, 1, 2],
    [2, 0, 2, 1, 2, 2],

    // vertical lines
    [0, 0, 1, 0, 2, 0],
    [0, 1, 1, 1, 2, 1],
    [0, 2, 1, 2, 2, 2]

    // top-left to bottom-right
    [0, 0, 1, 1, 2, 2],

    // bottom-left to top-right
    [2, 0, 1, 1, 0, 2]
  ]

  for (let i = 0; i < lines.length; i++) {
    let line = lines[i]
    if (checkThree(line[0], line[1], line[2], line[3], line[4], line[5])) {
      return true
    }
  }

  return false
}
```