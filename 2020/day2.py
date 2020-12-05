with open('day2_input.txt') as f:
    a = f.readlines()
count = 0
count2 = 0
for line in a:
    numbers, letters, word = line.split()
    minnum, maxnum = numbers.split('-')
    letter = letters[0]
    # Part 1
    if int(minnum) <= word.count(letter) <= int(maxnum):
        count += 1

    # Part 2
    if (word[int(minnum)-1] == letter) ^ (word[int(maxnum)-1] == letter):
        count2 += 1
        
print(count)
print(count2)



