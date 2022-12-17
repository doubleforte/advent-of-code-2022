# https://adventofcode.com/2022/day/5

import re


def parse_step(step: str):
    pattern = re.compile(r'(\d+)')
    matches = pattern.findall(step)
    matches = [int(x) for x in matches]
    return {
        'count': matches[0],
        'from': matches[1],
        'to': matches[2],
    }


def parse_diagram(diagram: str):
    last_line = diagram.split('\n')[-1]

    # Set up stacks array.
    stacks = {int(x): [] for x in last_line.replace(' ', '')}

    # Load crates into stack arrays.
    stack_indexes = [index for index, x in enumerate(last_line) if x != ' ']
    for row in diagram.split('\n')[:-1]:
        i = 1
        for index in stack_indexes:
            if 0 <= index < len(row):
                if row[index] != ' ':
                    stacks[i].insert(0, row[index])
            i += 1

    return stacks


def split_list(list: list, index) -> list[list]:
    first = list[:-index]
    second = list[-index:]
    return [first, second]


def get_top_crates(stacks: dict[int, list]):
    top_crates = ''

    for key, value in stacks.items():
        top_crates += value[-1]

    return top_crates


with open('day5/data.txt', 'r') as file:
    diagram, steps = file.read().split('\n\n')
    stacks = parse_diagram(diagram)

    # Parse steps.
    steps = steps.strip().split('\n')

    # Do the moves.
    for step in steps:
        step = parse_step(step)
        stack = stacks[step['from']]
        count = step['count']

        # 0 is a noop -- nothing to move.
        if count == 0:
            continue

        rest, crates = split_list(stack, count)

        # crates.reverse()
        stacks[step['to']] += crates
        stacks[step['from']] = rest

    print(f'Top crates: {get_top_crates(stacks)}')  # PRTTGRFPB
