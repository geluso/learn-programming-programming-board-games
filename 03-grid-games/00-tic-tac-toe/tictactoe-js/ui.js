export function displayBoard(game) {
  // if the mark is null return an empty string, otherwise return the original value
  const replaceNulls = mark => mark === null ? ' ' : mark

  // [f(x) if condition else g(x) for x in sequence]
  let [q, w, e] = game.board[0].map(replaceNulls)
  let [a, s, d] = game.board[1].map(replaceNulls)
  let [z, x, c] = game.board[2].map(replaceNulls)

  const lines = [
    ``,
    ` ${q} | ${w} | ${e}   q w e`,
    `---+---+---`,
    ` ${a} | ${s} | ${d}   a s d`,
    `---+---+---`,
    ` ${z} | ${x} | ${c}   z x c`
  ]

  lines.forEach(line => {
    displayMessage(line)
  })
}


export function displayMessage(text) {
  const out = document.getElementById('output')
  out.textContent += text + "\n"
}