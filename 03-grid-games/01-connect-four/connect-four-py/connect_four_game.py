EMPTY = "."


class ConnectFourGame:

    def __init__(self):
        self.reset()

    def reset(self):
        self.is_game_over = False
        self.winner = None

        self.turn = 0
        self.players = ["X", "O"]

        self.board = [
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        ]

    def make_move(self, col):
        if not self.is_valid(col=col):
            return False

        player = self.get_current_player()
        is_dropped = self.drop(col, player)
        if is_dropped:
            self.turn += 1
            if self.is_winning():
                self.is_game_over = True
                self.winner = player
            elif self.turn == 35:
                # the game ends if the board has filled up
                self.winner = None
                self.is_game_over = True

    def get_current_player(self):
        index = self.turn % len(self.players)
        player = self.players[index]
        return player

    def get(self, row, col):
        if not self.is_valid(row, col):
            return EMPTY
        return self.board[row][col]

    def is_valid(self, row=0, col=0):
        if row < 0 or row >= len(self.board):
            return False
        if col < 0 or col >= len(self.board[row]):
            return False
        return True

    def drop(self, col, token):
        if not self.is_valid(col=col):
            return False

        row = len(self.board) - 1
        is_placed = False

        while row >= 0 and not is_placed:
            if self.board[row][col] == EMPTY:
                self.board[row][col] = token
                is_placed = True
            row -= 1

        # return whether or not the token was actually placed
        return is_placed

    def is_winning(self):
        has_winner = self.search()
        if has_winner:
            return True

    def search(self):
        rows, cols = 5, 7
        for row in range(rows):
            for col in range(cols):
                is_winning = self.jig(row, col)
                if is_winning:
                    return True
        return False

    def jig(self, row, col):
        # gah, the lines were just too long when using "row" and "col"
        r, c = row, col

        # horizontal, vertical, forward-slash "\", back-slash "/"
        h1, h2, h3, h4 = [r+0, c+0], [r+0, c+1], [r+0, c+2], [r+0, c+3]
        v1, v2, v3, v4 = [r+0, c+0], [r+1, c+0], [r+2, c+0], [r+3, c+0]
        f1, f2, f3, f4 = [r+0, c+0], [r+1, c+1], [r+2, c+2], [r+3, c+3]
        b1, b2, b3, b4 = [r+0, c+3], [r+1, c+2], [r+2, c+1], [r+3, c+0]

        is_h = self.four_match(h1, h2, h3, h4)
        is_v = self.four_match(v1, v2, v3, v4)
        is_f = self.four_match(f1, f2, f3, f4)
        is_b = self.four_match(b1, b2, b3, b4)
        return is_h or is_v or is_f or is_b

    def four_match(self, c1, c2, c3, c4):
        p1 = self.get(c1[0], c1[1])
        p2 = self.get(c2[0], c2[1])
        p3 = self.get(c3[0], c3[1])
        p4 = self.get(c4[0], c4[1])

        p1_is_not_none = p1 is not EMPTY
        all_match = p1 == p2 and p2 == p3 and p3 == p4
        return p1_is_not_none and all_match
