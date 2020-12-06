with open('day5_input.txt') as f:
    a = f.readlines()

a.sort()
# for i in a:
#     print(i,end='')

answer = 'BBBFBBBRRR'
total = 0
for index, letter in enumerate(answer[-4::-1]):
    print(letter, index)
    if letter == 'B':
        total += 2**index
    print(total)

print(total)
result = 8*total +7
print(result)

