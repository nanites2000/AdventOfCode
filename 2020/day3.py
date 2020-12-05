with open('day3_input.txt') as f:
    a = f.readlines()
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1
for pair in slopes:
    count = 0
    for index, line in enumerate(a[pair[1]::pair[1]]):
        line = line.strip()*10000 # makes line long enough
        # instead the index could get moded by the line length
        if line[pair[0]*(index+1)] == '#':
            count += 1

    product = product * count
    print("count",count)
    print('product', product)