with open('day1/data.txt', 'r') as file:
    lines = file.read()

elves = lines.split('\n\n')
elf_totals = []

for elf in elves:
    items = elf.strip().split('\n')
    as_numbers = [int(x) for x in items]
    elf_calories = sum(as_numbers)
    elf_totals.append(elf_calories)

elf_totals.sort(reverse=True)

# Part 1: Real answer: 73211. Sample answer: 24000.
print(f'Most calories: {max(elf_totals)}')

number_of_safety_elves = 3
top_total = sum(elf_totals[:number_of_safety_elves])

# Part 2: Real answer: 213958. Sample answer: 45000.
print(f'Top {number_of_safety_elves} total: {top_total}')
