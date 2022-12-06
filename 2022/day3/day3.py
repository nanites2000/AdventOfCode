with open("input.txt") as input:
    lines = input.readlines()

#priority = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def find_prioority(character):
    return priority.index(character) + 1

total = 0
for line in lines:
    line_length = len(line)
    half = int((line_length-1) / 2)
    #print(half)
    #print(f"{line[0:half]}  {line[half:]}")
    first = set(line[0:half])
    second = set(line[half:])
    print(first & second)
    total += find_prioority(list(first & second)[0])
print(total)