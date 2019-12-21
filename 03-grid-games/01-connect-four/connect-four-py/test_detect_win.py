def search(grid):
    rows, cols = 5, 7
    for row in range(rows):
        for col in range(cols):
            is_winning = jig(grid, row, col)
            if is_winning:
                return True
    return False


def jig(grid, row, col):
    # gah, the lines were just too long when using "row" and "col"
    r, c = row, col

    # horizontal, vertical, forward-slash "\", back-slash "/"
    h1, h2, h3, h4 = [r+0, c+0], [r+0, c+1], [r+0, c+2], [r+0, c+3]
    v1, v2, v3, v4 = [r+0, c+0], [r+1, c+0], [r+2, c+0], [r+3, c+0]
    f1, f2, f3, f4 = [r+0, c+0], [r+1, c+1], [r+2, c+2], [r+3, c+3]
    b1, b2, b3, b4 = [r+0, c+3], [r+1, c+2], [r+2, c+1], [r+3, c+0]

    is_h = four_match(grid, h1, h2, h3, h4)
    is_v = four_match(grid, v1, v2, v3, v4)
    is_f = four_match(grid, f1, f2, f3, f4)
    is_b = four_match(grid, b1, b2, b3, b4)
    return is_h or is_v or is_f or is_b


def four_match(grid, c1, c2, c3, c4):
    p1 = get(grid, c1[0], c1[1])
    p2 = get(grid, c2[0], c2[1])
    p3 = get(grid, c3[0], c3[1])
    p4 = get(grid, c4[0], c4[1])

    p1_is_not_none = p1 is not None
    all_match = p1 == p2 and p2 == p3 and p3 == p4
    return p1_is_not_none and all_match


def is_valid(row, col):
    if row < 0 or col < 0 or row >= 5 or col >= 7:
        return False
    return True


def get(grid, row, col):
    if not is_valid(row, col):
        return None
    return grid[row][col]


grid1 = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
]

grid2 = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    ["X", "X", "X", "X", None, None, None],
]

grid3 = [
    [None, None, None, None, None, None, None],
    ["X", None, None, None, None, None, None],
    ["X", None, None, None, None, None, None],
    ["X", None, None, None, None, None, None],
    ["X", None, None, None, None, None, None],
]

grid4 = [
    [None, None, None, None, None, None, None],
    ["O", None, None, None, None, None, None],
    ["X", "O", None, None, None, None, None],
    ["X", "X", "O", None, None, None, None],
    ["X", "X", "X", "O", None, None, None],
]

grid5 = [
    [None, None, None, None, None, None, None],
    [None, None, None, "O", None, None, None],
    [None, None, "O", "X", None, None, None],
    [None, "O", "X", "X", None, None, None],
    ["O", "X", "X", "X", None, None, None],
]

grid6 = [
    [None, None, None, None, None, None, "X"],
    [None, None, None, None, None, "X", None],
    [None, None, None, None, "X", None, None],
    [None, None, None, "X", None, None, None],
    [None, None, None, None, None, None, None],
]

grid7 = [
    ["X", None, None, None, None, None, None],
    ["X", "X", None, None, None, None, None],
    ["O", "O", "X", None, None, None, None],
    ["X", "X", "X", "O", "O", "O", "X"],
    ["X", "O", "O", "X", "X", "X", "O"],
]

grids = [grid1, grid2, grid3, grid4, grid5, grid6, grid7]
for grid in grids:
    is_win = search(grid)
    print("is win?", is_win)
