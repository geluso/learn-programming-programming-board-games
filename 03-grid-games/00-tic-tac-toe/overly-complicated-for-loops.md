Notice I'm writing this with some for-loops starting at `1` as my preferred
way of preventing array-index-out-of-bounds errors. (I'm having the for-loop
start a bit ahead and looking behind itself as it walks forward to the end of
the array.)

```js
// check each row across
for (let row = 0; row < board.length; row++) {
  let threeHorizontal = true

  for (let col = 1; col < board[row].length; col++) {
    const column1 = board[row][col - 1]
    const column2 = board[row][col]

    const isNull = column1 === null || column2 === null
    const isMatching = column1 === column2

    if () {

    }  
  }
}
```
