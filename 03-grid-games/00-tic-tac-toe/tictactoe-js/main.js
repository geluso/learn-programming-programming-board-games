import { displayBoard, displayMessage } from './ui.js'
import TicTacToeGame from './tic_tac_toe_game.js'


function letterToCoordinate(letter) {
  const mapping = {
    "q": [0, 0], "w": [0, 1], "e": [0, 2],
    "a": [1, 0], "s": [1, 1], "d": [1, 2],
    "z": [2, 0], "x": [2, 1], "c": [2, 2],
  }
  return mapping[letter]
}


function displayWinner(game) {
  displayBoard(game)

  if (game.players.includes(game.winner)) {
    displayMessage("%s wins!" % game.winner)
  } else {
    displayMessage("CATS! The game ended in a tie.")
  }
}

function handleInput(ev, game) {
  ev.preventDefault()

  const input = ev.target.elements.input.value
  const choice = letterToCoordinate(input)

  ev.target.elements.input.value = ''

  if (choice === undefined) {
    displayMessage("Invalid choice! Enter a letter.")
  } else {
    let [row, col] = choice
    game.makeMove(row, col)
  }

  displayBoard(game)
  if (game.isGameOver) {
    displayWinner(game)
  }
}

function main() {
  const game = new TicTacToeGame()
  displayBoard(game)

  const form = document.getElementById('input')
  form.addEventListener('submit', ev => {
    handleInput(ev, game)
  })
}


main()
