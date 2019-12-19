def split_num(value):
    result = []
    for i in range(5,-1,-1):
        divisor = 10**i
        digit = (math.floor(value/divisor))
        result.append(digit)
        value -= divisor * digit
    return(result)

for k in range(99,0,-1):
    for j in range(99,0,-1):
        instructions = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0]
        instructions[1] = k
        instructions[2] = j


        def add(i1,i2,iresult):
            global instructions
            sum = instructions[i1] +instructions[i2]
            instructions[iresult] = sum

        def mult(i1,i2,iresult):
            global instructions
            product = instructions[i1] * instructions[i2]
            instructions[iresult] = product

        for i in range(0,len(instructions),4):
            if instructions[i] == 1:
                add(instructions[i+1],instructions[i+2],instructions[i+3])
                length = 4
            elif instructions[i] == 2:
                mult(instructions[i + 1], instructions[i + 2], instructions[i + 3])
                length = 4
            elif instructions[i] == 3:
                length = 2
            elif instructions[i] == 4:
                length = 2
            elif instructions == 99:
                break

        if instructions[0] == 19690720:
            print (instructions)