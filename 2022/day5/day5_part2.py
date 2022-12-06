

with open("input.txt") as input:
    lines = input.readlines()

rows = [
    [0],
    ['t','d','w','z','v','p'],
    ['l','s','w','v','f','j','d'],
    ['z','m','l','s','v','t','b','h'],
    ['r','j','s'],
    ['c','z','b','g','f','m','l','w'],
    ['q','w','v','h','z','r','g','b'],
    ['v','j','p','c','b','d','n'],
    ['p','t','b','q'],
    ['h','g','z','r','c'],
    ]

for line in lines:
    # split the numbers up
    group1, group2 = line.split(' from ')
    garbage, move_number = group1.split()
    start_row, end_row = group2.split(' to ')
    move_number = int(move_number)
    start_row = int(start_row)
    end_row = int(end_row)
    # print(move_number, start_row, end_row)

    # find the spring to move and add to the next list
    lifted_string = []
    for i in range(0,move_number):
        #print(rows[start_row])
        lifted_string.append(rows[start_row].pop())
    lifted_string.reverse()
    print(lifted_string)
    rows[end_row].extend(lifted_string)

for i in rows:
        print(i[-1])
