export default class TicTacToeGame {
  constructor() {
    this.resetGame()
  }

  resetGame() {
    this.winner = null
    this.isGameOVer = false

    this.turn = 0
    this.players = ["X", "O"]

    this.board = [
      [null, null, null],
      [null, null, null],
      [null, null, null],
    ]
  }

  getCurrentPlayer() {
    const index = this.turn % this.players.length
    const player = this.players[index]
    return player
  }

  isValidMove(row, col) {
    if (row < 0 || col < 0 || row > 2 || col > 2) {
      return false
    }

    if (this.board[row][col] !== null) {
      return false
    }

    return true
  }

  makeMove(row, col) {
    if (this.isGameOver) {
      return
    }

    if (!this.isValidMove(row, col)) {
      return
    }

    // mark the board with the current player X or O
    const player = this.getCurrentPlayer()
    this.board[row][col] = player

    // check to see if the move ended the game
    if (this.hasWinner()) {
      this.isGameOVer = true
      this.winner = player
    } else if (this.turn == 8) {
      this.isGameOver = true
      this.winner = "tie"
    } else {
      this.turn += 1
    }
  }

  checkThree(row1, col1, row2, col2, row3, col3) {
    const isNotNull = this.board[row1][col1] !== null
    const oneMatchesTwo = this.board[row1][col1] === this.board[row2][col2]
    const twoMatchesThree = this.board[row2][col2] === this.board[row3][col3]
    const threeInARow = oneMatchesTwo && twoMatchesThree

    if (isNotNull && threeInARow) {
      return true
    }
    return false
  }

  hasWinner() {
    const lines = [
      // horizontal lines
      [0, 0, 0, 1, 0, 2],
      [1, 0, 1, 1, 1, 2],
      [2, 0, 2, 1, 2, 2],

      // vertical lines
      [0, 0, 1, 0, 2, 0],
      [0, 1, 1, 1, 2, 1],
      [0, 2, 1, 2, 2, 2],

      // top - left to bottom - right
      [0, 0, 1, 1, 2, 2],

      // bottom - left to top - right
      [2, 0, 1, 1, 0, 2]
    ]

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i]
      if (this.checkThree(line[0], line[1], line[2], line[3], line[4], line[5])) {
        return true
      }
    }
  }
}