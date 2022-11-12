var board = [
    [null, null, null, null null, null, null, null],
    [null, null, null, null null, null, null, null],
    [null, null, null, null null, null, null, null],
    [null, null, null, null null, null, null, null],
    [null, null, null, null null, null, null, null],
    [null, null, null, null null, null, null, null],
    [null, null, null, null null, null, null, null],
    [null, null, null, null null, null, null, null],
]

var board = [
    [new Rook(0), new Knight(0), new Bishop(0), new Queen(0), new King(0), new Bishop(0), new Knight(0), new Rook(0)],
    [new Pawn(0), new Pawn(0), new Pawn(0), new Pawn(0), new Pawn(0), new Pawn(0), new Pawn(0), new Pawn(0)],
    [null, null, null, null null, null, null, null],
    [null, null, null, null null, null, null, null],
    [null, null, null, null null, null, null, null],
    [null, null, null, null null, null, null, null],
    [new Pawn(1), new Pawn(1), new Pawn(1), new Pawn(1), new Pawn(1), new Pawn(1), new Pawn(1), new Pawn(1)],
    [new Rook(1), new Knight(1), new Bishop(1), new Queen(1), new King(1), new Bishop(1), new Knight(1), new Rook(1)],
]
let board = [];

// Set up black's pieces
let blackBackRow = [new Rook(0), new Knight(0), new Bishop(0), new Queen(0), new King(0), new Bishop(0), new Knight(0), new Rook(0)];
let blackFrontRow = new Array(8);
for (let i = 0; i < blackFrontRow.length; i++) {
    blackFrontRow[i] = new Pawn(0);
}

// Add four empty rows for the middle of the board
for (let i = 0; i < 4; i++) {
    board.push(new Array(8))
}

// Set up white's pieces
let backRow = [new Rook(0), new Knight(0), new Bishop(0), new Queen(0), new King(0), new Bishop(0), new Knight(0), new Rook(0)];
let frontRow = new Array(8);
for (let i = 0; i < frontRow.length; i++) {
    frontRow[i] = new Pawn(0);
}
function createPieces(color) {
    let frontRow = (new Array(8)).map(() => new Pawn());
    let backRow = [new Rook(), new Knight(), new Bishop(), new Queen(), new King(), new Bishop(), new Knight(), new Rook()];

    // add the color for each piece
    frontRow.forEach(piece => piece.color = color);
    backRow.forEach(piece => piece.color = color);

    return {frontRow, backRow};
}

function createBoard() {
    let board = new Array(8);
    let blackPieces = createPieces('black');
    let whitePieces = createPieces('white');

    board[0] = blackPieces.backRow;
    board[1] = blackPieces.frontRow;

    for (let i = 2; i < board.length - 2; i++) {
        board[i] = new Array(8);
    }

    board[board.length - 2] = whitePieces.frontRow;
    board[board.length - 1] = whitePieces.backRow;
}

function makeMoveByPosition(board, startPosition, endPosition) {
    let startIndex = positionToIndex(startPosition);
    let endIndex = positionToIndex(endPosition);
    makeMoveByIndex(board, startIndex.row, statIndex.col, endRow.row, endCol.col);
}

function makeMoveByIndex(board, startRow, startCol, endRow, endCol) {
    let startPiece = board[startRow][startCol];
    let endPiece = board[endRow][endCol];

    board[startRow][startCol] = null;
    board[endRow][endCol] = startPiece;
}

function isValidIndex(board, row, col) {
    if (row < 0 || col < 0) {
        return false;
    }

    if (row >= board.length) {
        return false;
    }

    if (row[col] >= board[row].length) {
        return false;
    }

    return true;
}

function makeMoveByIndex(board, startRow, startCol, endRow, endCol) {
    if (isValidIndex(board, startRow, startCol)) {
        return false;
    }

    if (isValidIndex(board, endRow, endCol)) {
        return false;
    }

    let startPiece = board[startRow][startCol];
    let endPiece = board[endRow][endCol];

    board[startRow][startCol] = null;
    board[endRow][endCol] = startPiece;

    return false;
}

function rookMoves(board, startRow, startCol) {
    let moves = [];

    // up
    let row = startRow;
    let col = startCol;
    let isBlocked = false;
    while (!blocked && row >= 0) {
        row -= 1;
        if (!isValidIndex(board, row, col)) {
            isBlocked = true;
        } else {
            let piece = board[row][col];
            if (piece.color === board[startRow][startCol].color) {
                isBlocked = true;
            } else {
                moves.push({row, col});
            }
        }
    }

    // down
    let row = startRow;
    let col = startCol;
    let isBlocked = false;
    while (!blocked && row >= 0) {
        row += 1;
        if (!isValidIndex(board, row, col)) {
            isBlocked = true;
        } else {
            let piece = board[row][col];
            if (piece.color === board[startRow][startCol].color) {
                isBlocked = true;
            } else {
                moves.push({row, col});
            }
        }
    }

    // left
    let row = startRow;
    let col = startCol;
    let isBlocked = false;
    while (!blocked && row >= 0) {
        col -= 1;
        if (!isValidIndex(board, row, col)) {
            isBlocked = true;
        } else {
            let piece = board[row][col];
            if (piece.color === board[startRow][startCol].color) {
                isBlocked = true;
            } else {
                moves.push({row, col});
            }
        }
    }

    // right
    let row = startRow;
    let col = startCol;
    let isBlocked = false;
    while (!blocked && row >= 0) {
        col += 1;
        if (!isValidIndex(board, row, col)) {
            isBlocked = true;
        } else {
            let piece = board[row][col];
            if (piece.color === board[startRow][startCol].color) {
                isBlocked = true;
            } else {
                moves.push({row, col});
            }
        }
    }


    return moves;
}

function movementSquares(board, startRow, startCol) {
    // search for moves in every direction
    const up = getSquaresInDirection(board, startRow, startCol, -1, 0);
    const down = getSquaresInDirection(board, startRow, startCol, 1, 0);
    const left = getSquaresInDirection(board, startRow, startCol, 0, -1);
    const right = getSquaresInDirection(board, startRow, startCol, 0, 1);
    return [...up, ...down, ...left, ...right];
}

function getSquaresInDirection(board, startRow, startCol, rowDirection, colDirection) {
    // create an array to collect all moves in this direction
    let moves = [];

    let steps = 0;
    let isSearching = true;
    while (isSearching) {
        steps++;

        let row = startRow + steps * rowDirection;
        let col = startCol + steps * colDirection;

        // stepped off the board
        if (!isValidIndex(row, col)) {
            isSearching = false;
        }

        // if the piece on this square is the same color as the starting piece
        // then the square is not added because we are blocked by our own piece
        let piece = board[row][col]
        if (piece.color !== board[startRow][startCol].color) {
            isSearching = false
        }

        moves.push({row, col});

        // stop searching if the row contained an enemy piece because the
        // furthest a piece can move is capturing that piece.
        if (piece !== null) {
            isSearching = false
        }
    }
    return moves;
}
