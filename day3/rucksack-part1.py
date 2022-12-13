# https://adventofcode.com/2022/day/3

import re

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

for bag in bags:
    compartment1 = bag[:len(bag) // 2]
    compartment2 = bag[len(bag) // 2:]

    in_common = list(set.intersection(*map(set, [compartment1, compartment2])))

    for item in in_common:
        value_list = lowercase_values if re.search(
            '[a-z]', item
        ) else uppercase_values

        running_total += value_list[item]

print(f'Total: {running_total}')  # 7997
