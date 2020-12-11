import copy
import numpy
with open('day10_example.txt') as f:
    a = [int(i.strip()) for i in f.readlines()]
a.append(0) #add this for the first 0v adaptor
a.sort()
print(a)
count_of_ones = 0
count_of_threes = 0
#part1
for index, value in enumerate(a[:-1]):
    if value + 1  == a[index+1]:
        count_of_ones += 1
    else:
        count_of_threes += 1
count_of_threes += 1 #for the final +3 to final adaptor
print(count_of_ones, count_of_threes)
print(count_of_threes * count_of_ones)

#part2
number_it_could_reach = []
a.append(max(a)+3)

for index, value in enumerate(a[:-1]):
    current_multiple = 0
    print(value)
    print(a[index+1:index+4])
    if value + 1 in a[index+1:index+4]:
        current_multiple += 1
    if value + 2 in a[index+1:index+4]:
        current_multiple += 1
    if value + 3 in a[index+1:index+4]:
        current_multiple += 1
    number_it_could_reach.append(current_multiple)
print(number_it_could_reach)
product = 1
for x in number_it_could_reach:
    product = product * x
print(product)
#print(numpy.prod(number_it_could_reach))