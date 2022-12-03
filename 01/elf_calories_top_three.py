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
top_three = []

for elf_calories in all_elves_calories:
    totals.append(sum(elf_calories))

for i in range(3):
    highest = max(totals)
    
    top_three.append(highest)
    num = totals.index(highest)
    del totals[num]


top_three_total = sum(top_three)

print(top_three_total)
