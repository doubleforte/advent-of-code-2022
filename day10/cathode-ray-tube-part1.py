# https://adventofcode.com/2022/day/10


def get_signal_strength(cycle_count: int, x_value: int) -> int:
    return cycle_count * x_value


def run_cycle(x):
    global cycle_count

    cycle_count += 1
    if cycle_count in CHECKING:
        interesting_cycle_x_values.append(get_signal_strength(cycle_count, x))


with open('day10/data.txt') as file:
    lines = [line.strip() for line in file.readlines()]

CHECKING = [20, 60, 100, 140, 180, 220]

x = 1
cycle_count = 0

interesting_cycle_x_values: list[int] = []

for line in lines:
    line = line.split(' ')

    if line[0] == 'addx':

        run_cycle(x)
        # Do it again because addr takes two.
        run_cycle(x)

        value = int(line[1])
        x += value
    else:
        run_cycle(x)

print(f'Signal sum: {sum(interesting_cycle_x_values)}')  # 13680
