# https://adventofcode.com/2022/day/8

with open('day8/data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

scenic_scores: list[int] = []

for row, trees in enumerate(lines):
    trees = [int(x) for x in trees]

    for column, tree in enumerate(trees):
        if any([
            column == 0,
            row == 0,
            column == len(trees) - 1,
            row == len(lines) - 1,
        ]):
            continue  # Edges have a 0, so multiplying will just be zero. Ignore.

        left = trees[:column]
        right = trees[column + 1:len(trees)]
        up = [int(i[column]) for i in lines[:row]]
        down = [int(i[column]) for i in lines[row + 1:]]

        # We are looking away from the tree in different directions.
        left.reverse()
        up.reverse()

        tree_score = 1

        for direction in (left, right, up, down):
            counter = 0
            for i in direction:
                if i < tree:
                    counter += 1
                elif i >= tree:
                    counter += 1
                    break

            tree_score *= counter

        scenic_scores.append(tree_score)

print(f'Max visible score: {max(scenic_scores)}')  # 230112
