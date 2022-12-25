# https://adventofcode.com/2022/day/9
# https://www.youtube.com/watch?v=QfSPVrWKGcU


def is_touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move(dx, dy):
    global knots

    knots[0][0] += dx
    knots[0][1] += dy

    for i in range(1, KNOT_COUNT):
        hx, hy = knots[i - 1]
        tx, ty = knots[i]

        if not is_touching(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += sign_x
            ty += sign_y

        knots[i] = [tx, ty]


with open('day9/data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

KNOT_COUNT = 10

# Globals. Current positions.
knots = [[0, 0] for _ in range(KNOT_COUNT)]

# All possible moves map.
dd = {
    'R': [1, 0],
    'U': [0, 1],
    'L': [-1, 0],
    'D': [0, -1],
}

tail_visited = set()
tail_visited.add(tuple(knots[-1]))

for line in lines:
    op, amount = line.split(' ')
    amount = int(amount)
    dx, dy = dd[op]

    # Move one step for each step. R2 = right twice, so do it twice.
    for _ in range(amount):
        move(dx, dy)
        tail_visited.add(tuple(knots[-1]))

print(f'Total positions: {len(tail_visited)}')  # 6067
