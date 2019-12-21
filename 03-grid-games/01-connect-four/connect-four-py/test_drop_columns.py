from connect_four_game import ConnectFourGame

COLUMN_MAX_TOKENS = 5


def drop(columns, col, token):
    # check to make sure it's a legitimate column index
    if col < 0 or col >= len(columns):
        return False

    # check to make sure the column isn't full
    if len(columns[col]) >= COLUMN_MAX_TOKENS:
        return False

    # add the token to the end and report success!
    columns[col].append(token)
    return True


def display_columns(columns):
    print("1  2  3  4  5  6  7")
    row = 4
    while row >= 0:
        line = ""
        for col in range(0, 7):
            if len(columns[col]) <= row:
                line += ".  "
            else:
                line += columns[col][row] + "  "

        print(line)
        row -= 1


test_drop_columns = [
    [],
    ["0"],
    ["0", "0"],
    ["0", "0", "0"],
    ["0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    [],
]

token = "X"
for column in range(-2, 10):
    result = drop(test_drop_columns, column, token)
    print("drop in column", column, result)

display_columns(test_drop_columns)
