# https://adventofcode.com/2022/day/8

with open('day8/data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

# def dedup_list(og_list):
#     return [list(y) for y in set([tuple(x) for x in og_list])]

visibles: list[int, int] = []  # column, row

for row, trees in enumerate(lines):
    trees = [int(x) for x in trees]

    for column, tree in enumerate(trees):
        # Anything on the outside edge is visible.
        if any([
            column == 0,
            row == 0,
            column == len(trees) - 1,
            row == len(lines) - 1,
        ]):
            visibles.append([column, row])
            continue  # No need to carry on.

        left = trees[:column]
        right = trees[column + 1:len(trees)]
        up = [int(i[column]) for i in lines[:row]]
        down = [int(i[column]) for i in lines[row + 1:]]

        if any([
            max(left) < tree,
            max(right) < tree,
            max(up) < tree,
            max(down) < tree,
        ]):
            visibles.append([column, row])

print(f'Number of visible trees: {len(visibles)}')
