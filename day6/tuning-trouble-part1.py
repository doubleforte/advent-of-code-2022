# https://adventofcode.com/2022/day/6

import re

with open('day6/data.txt', 'r') as file:
    stream = file.read().strip()

i = 0
length_of_marker = 4
pattern = r'^(?:([A-Za-z])(?!.*\1))*$'  # All unique characters?

while i < len(stream):
    quad = stream[i:length_of_marker + i]

    if re.match(pattern, quad):
        print(f'Marker complete at {i + length_of_marker}')  # 1566
        break

    i += 1
