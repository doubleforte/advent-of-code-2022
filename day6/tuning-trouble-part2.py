# https://adventofcode.com/2022/day/6

with open('day6/data.txt', 'r') as file:
    stream = file.read().strip()

i = 0
length_of_marker = 14

while i < len(stream):
    group = stream[i:length_of_marker + i]

    if len(set(group)) == length_of_marker:
        print(f'Marker complete at {i + length_of_marker}')  # 2265
        break

    i += 1
