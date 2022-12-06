
with open("input.txt") as input:
    lines = input.readlines()

elfs = []
print(lines)

sum = 0
for line in lines:
    line = line.strip()

    if line:
        sum += int(line)
    else:
        elfs.append(sum)
        print(sum)
        sum = 0

maximum = max(elfs)
print(f"Maximum is: {maximum}")
max_index = elfs.index(maximum)
print(f"Most valuable elf is: {max_index+1}th elf")

elfs.pop(max_index)
maximum2 = max(elfs)
print(f"Maximum is: {maximum2}")
max_index = elfs.index(maximum2)
print(f"Most valuable elf is: {max_index+1}th elf")

elfs.pop(max_index)
maximum3 = max(elfs)
print(f"Maximum is: {maximum3}")
max_index = elfs.index(maximum3)
print(f"Most valuable elf is: {max_index+1}th elf")

print(f"Sum of the top three elfs: {maximum + maximum2 + maximum3}")