import copy
with open('day8_input.txt') as f:
    a = f.readlines()
# a =[
# 'nop +0',
# 'acc +1',
# 'jmp +4',
# 'acc +3',
# 'jmp -3',
# 'acc -99',
# 'acc +1',
# 'jmp -4',
# 'acc +6',
# ]
data = []
for row in a:
    instruction, num_string = row.split()
    data.append([instruction, int(num_string)])
current = 0
accum = 0
previous_currents = []
day = 2

if day == 1:
    while True:
        print(current, accum)
        if current in previous_currents:
            break
        else:
            previous_currents.append(current)

        if data[current][0] == 'nop':
            current += 1
        elif data[current][0] == 'acc':
            accum += data[current][1]
            current += 1

        elif data[current][0] == 'jmp':
            current += data[current][1]

    print('accum: ',accum)


def terminates(data):
    print('----------------------------------------------------------------------------')
    terminal = False
    total_steps = 0
    current = 0
    accum = 0
    previous_currents = []
    try:
        while total_steps < 10000:
            if current in previous_currents:
                return False
            # print(current, accum)
            if data[current][0] == 'nop':
                current += 1
            elif data[current][0] == 'acc':
                accum += data[current][1]
                current += 1
            elif data[current][0] == 'jmp':
                current += data[current][1]
            #print(accum)
            total_steps += 1
            #print(total_steps)
    except:
        return accum




original_data = copy.copy(data)
print(original_data)
if day == 2:

    max_row = len(a)
    print(data)
    for index, row in enumerate(data):
        print(original_data)
        data = copy.deepcopy(original_data)
        total_steps = 0
        current = 0
        accum = 0
        max_row = len(a)
        #print(data)
        if row[0] == 'nop':
            data[index][0] = 'jmp'
        elif row[0] == 'jmp':
            data[index][0] = 'nop'
        #print(data)
        result = terminates(data)
        if result:
            print("-----------------------------------------------------------------------")
            print(result)
            break
