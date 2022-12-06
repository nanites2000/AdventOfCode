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



    if onea <= twoa and oneb >= twob:
        total += 1
        print(line.strip())
    elif twoa <= onea and twob >= oneb:
        total += 1
        print(line.strip())
    # print(onea, oneb, twoa, twob)


print(total)

