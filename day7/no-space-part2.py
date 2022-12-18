# https://adventofcode.com/2022/day/7
# Adapted from https://www.youtube.com/watch?v=XvA0iO_gvfM

with open('day7/data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

TOTAL_SPACE = 70000000
MIN_REQUIRED_SPACE = 30000000

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


def get_dir_size(dir=root):
    # It's a file
    if type(dir) == int:
        return dir
    return sum(map(get_dir_size, dir.values()))


threshold = get_dir_size() - (TOTAL_SPACE - MIN_REQUIRED_SPACE)


def do_it(dir=root):
    puzzle_response = float('inf')

    if get_dir_size(dir) >= threshold:
        puzzle_response = get_dir_size(dir)

    for child in dir.values():
        if type(child) == int:
            continue
        q = do_it(child)
        puzzle_response = min(puzzle_response, q)
    return puzzle_response


print(f'Answer: {do_it()}')  # 9847279
