import copy
with open('day9_input.txt') as f:
    a = [i.strip() for i in f.readlines()]
data = []
print(a)
day = 2
if day == 1:
    for index, row in enumerate(a[25:]):
        found = False
        for x in a[0+index:25+index]:
            # print(index, row, x)
            # print(a[0 + index:25 + index])
            if str(int(row) - int(x)) in a[0+index:25+index]:
                found = True
                #print(index)
                pass
        if not found:
            print('index= ', index)
            print(a[25+index])
if day == 2:
    for index, row in enumerate(a[:557]):
        sum = 0
        index2 = index
        while sum < int(a[557]):
            print(sum)
            sum += int(a[index2])
            index2 += 1
        if sum == a[557]:
            print(index, index2)
            #break
