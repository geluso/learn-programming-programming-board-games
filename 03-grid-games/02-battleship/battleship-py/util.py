from random import choice


def direction_to_dx_dy(direction):
    dx, dy = 0, 0
    if direction == "right":
        dx = 1
    if direction == "down":
        dy = 1
    if direction == "left":
        dx = -1
    if direction == "up":
        dy = -1
    return dx, dy


def random_row_col_direction():
    rows = "ABCDEFGH"
    cols = "123456789"
    directions = ["right", "left", "up", "down"]

    row = choice(rows)
    col = choice(cols)
    direction = choice(directions)

    row = rows.index(row)
    col = cols.index(col)

    return row, col, direction
