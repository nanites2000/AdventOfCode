import copy
with open('day9_input.txt') as f:
    a = [i.strip() for i in f.readlines()]

# a=[
# 35,
# 20,
# 15,
# 25,
# 47,
# 40,
# 62,
# 55,
# 65,
# 95,
# 102,
# 117,
# 150,
# 182,
# 127,
# 219,
# 299,
# 277,
# 309,
# 576,
#     ]
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
        print(a[556])
        sum = 0
        index2 = index
        current_range = []
        while sum < 177777905:  #int(a[557]):
            current_range.append(int(a[index2]))
            sum += int(a[index2])
            index2 += 1
            print(sum)
        if sum == 177777905: # a[557]:
            print(min(current_range), max(current_range))
            print((min(current_range) + max(current_range)))
            break
