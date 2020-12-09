with open('day8_input.txt') as f:
    a = f.readlines()
a =[
'nop +0',
'acc +1',
'jmp +4',
'acc +3',
'jmp -3',
'acc -99',
'acc +1',
'jmp -4',
'acc +6',
]
data = []
for row in a:
    instruction, num_string = row.split()
    data.append((instruction, int(num_string)))
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

if day == 2:
    max_row = len(a)
    for row in a:
        total_steps = 0
        current = 0
        accum = 0
        max_row = len(a)
        if row[0] == 'nop':
            row[0] == 'jmp'
        elif row[0] == 'jmp':
            row[0] == 'nop'

        while total_steps < 10000:
           # print(current, accum)

            if data[current][0] == 'nop':
                current += 1
            elif data[current][0] == 'acc':
                accum += data[current][1]
                current += 1

            elif data[current][0] == 'jmp':
                current += data[current][1]
            print(accum)
            total_steps += 1
            if current >= max_row:
                print('Finished!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                break


# 34166 too high