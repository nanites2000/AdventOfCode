with open("input.txt") as input:
    lines = input.readlines()

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def find_prioority(character):
    return priority.index(character) + 1

total = 0



for index, line in enumerate(lines):
    if index % 3 == 0:
        first = set(line.strip())
    elif index % 3 == 1:
        second = set(line.strip())
    else:
        third = set(line.strip())
        print(first & second & third)
        total += find_prioority(list(first & second & third)[0])
print(total)