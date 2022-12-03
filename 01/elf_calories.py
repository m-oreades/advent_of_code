all_elves_calories = []

def add_elf():
    all_elves_calories.append([])

    
with open('data.txt', 'r') as file:
    add_elf()
    for line in file:
        if line == '\n':
            add_elf()
        else:
            all_elves_calories[-1].append(int(line))

totals = []

for elf_calories in all_elves_calories:
    totals.append(sum(elf_calories))

highest = max(totals)

print(highest)
