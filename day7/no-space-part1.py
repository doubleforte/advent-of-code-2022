# https://adventofcode.com/2022/day/7
# Adapted from https://www.youtube.com/watch?v=XvA0iO_gvfM

with open('day7/data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

MAX_SIZE = 100000

cwd = root = {}
stack = []

for line in lines:
    line = line.split(' ')

    if line[0] == '$':
        # Handle changing dirs
        if line[1] == 'cd':
            dir = line[2]

            if dir == '/':
                cwd = root
                stack = []

            elif dir == '..':
                cwd = stack.pop()

            else:
                if dir not in cwd:
                    cwd[dir] = {}
                stack.append(cwd)
                cwd = cwd[dir]

        # Handle ls
        elif line[1] == 'ls':
            pass

    # Handle dir contents
    else:
        a, b = [line[0], line[1]]

        if a == 'dir':
            if b not in cwd:
                cwd[b] = {}

        else:
            cwd[b] = int(a)


def do_it(dir=root):
    # It's a file
    if type(dir) == int:
        return (dir, 0)

    size = 0
    puzzle_response = 0

    # Recursive is fun.
    for child in dir.values():
        s, p = do_it(child)
        size += s
        puzzle_response += p

    if size <= MAX_SIZE:
        puzzle_response += size

    return (size, puzzle_response)


print(f'Total sizes: {do_it(root)[1]}')  # 1315285
