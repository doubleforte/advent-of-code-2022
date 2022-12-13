# https://adventofcode.com/2022/day/3

import re


def get_item_value(item):
    value_list = lowercase_values if re.search(
        '[a-z]', item
    ) else uppercase_values
    return value_list[item]


alphabet = 'abcdefghijklmnopqrstuvwxyz'

lowercase_values = dict()
for index, letter in enumerate(alphabet):
    lowercase_values[letter] = index + 1

uppercase_values = dict()
for index, letter in enumerate(alphabet.upper()):
    uppercase_values[letter] = index + 27

with open('day3/data.txt', 'r') as file:
    bags = file.read().splitlines()

running_total = 0
elves_per_group = 3

elf_count = 0
elf_groups = []
current_group = []

# Put elves in groups.
for bag in bags:
    if elf_count % elves_per_group == 0:
        if (len(current_group) > 0):
            current_group = []  # Start a new group.
        elf_groups.append(current_group)  # Add it to the Done pile.

    current_group.append(bag)

    elf_count += 1

for group in elf_groups:
    in_common = list(set.intersection(*map(set, group)))

    for item in in_common:
        running_total += get_item_value(item)

print(f'Total: {running_total}')  # 2545
