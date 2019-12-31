
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
