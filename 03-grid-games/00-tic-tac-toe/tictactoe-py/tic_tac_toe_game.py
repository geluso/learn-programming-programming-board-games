class TicTacToeGame:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.winner = None
        self.is_game_over = False

        self.turn = 0
        self.players = ["X", "O"]

        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def get_current_player(self):
        index = self.turn % len(self.players)
        player = self.players[index]
        return player

    def is_valid_move(self, row, col):
        if row < 0 or col < 0 or row > 2 or col > 2:
            return False

        if self.board[row][col] is not None:
            return False

        return True

    def make_move(self, row, col):
        if self.is_game_over:
            return

        if not self.is_valid_move(row, col):
            return

        # mark the board with the current player X or O
        player = self.get_current_player()
        self.board[row][col] = player

        # check to see if the move ended the game
        if self.has_winner():
            self.is_game_over = True
            self.winner = player
        elif self.turn == 8:
            self.is_game_over = True
            self.winner = "tie"
        else:
            self.turn += 1

    def check_three(self, row1, col1, row2, col2, row3, col3):
        board = self.board

        isNotNull = board[row1][col1] is not None
        oneMatchesTwo = board[row1][col1] is board[row2][col2]
        twoMatchesThree = board[row2][col2] is board[row3][col3]
        threeInARow = oneMatchesTwo and twoMatchesThree

        if isNotNull and threeInARow:
            return True
        return False

    def has_winner(self):
        lines = [
            # horizontal lines
            [0, 0, 0, 1, 0, 2],
            [1, 0, 1, 1, 1, 2],
            [2, 0, 2, 1, 2, 2],

            # vertical lines
            [0, 0, 1, 0, 2, 0],
            [0, 1, 1, 1, 2, 1],
            [0, 2, 1, 2, 2, 2],

            # top-left to bottom-right
            [0, 0, 1, 1, 2, 2],

            # bottom-left to top-right
            [2, 0, 1, 1, 0, 2]
        ]

        for line in lines:
            if self.check_three(line[0], line[1], line[2], line[3], line[4], line[5]):
                return True
        return False
