# https://adventofcode.com/2022/day/4


def inclusive_range(start: int, stop: int) -> range:
    step = 1
    return range(start, stop + step, step)


def create_range_from_string(string: str) -> range:
    parts = [int(x) for x in string.split('-')]
    return inclusive_range(parts[0], parts[1])


def is_either_a_subset(range1: range, range2: range) -> bool:
    set1 = set(range1)
    set2 = set(range2)
    return set1.issubset(set2) or set2.issubset(set1)


with open('day4/data.txt', 'r') as file:
    pairs = file.read().splitlines()

running_count = 0

for pair_string in pairs:
    pair = pair_string.split(',')

    elf1 = create_range_from_string(pair[0])
    elf2 = create_range_from_string(pair[1])

    if is_either_a_subset(elf1, elf2):
        running_count += 1

print(f'Total engulfs: {running_count}')  # 496
