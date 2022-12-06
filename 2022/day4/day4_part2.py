with open("input.txt") as input:
    lines = input.readlines()

total = 0

for line in lines:
    line = line.strip()
    one, two = line.split(',')
    onea, oneb = one.split('-')
    twoa, twob = two.split('-')
    onea = int(onea)
    oneb = int(oneb)
    twoa = int(twoa)
    twob = int(twob)

   #print(onea, oneb, twoa, twob)
    list1 = []
    for i in range(onea, oneb+1):
        list1.append(i)

    list2 = []
    for i in range(twoa, twob+1):
        list2.append(i)

    if len(set(list1) & set(list2)) > 0:
        print(line)
        total += 1
    print(set(list1) & set(list2))


print(total)