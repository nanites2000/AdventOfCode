

def go_up(start,distance):
    """
    start is a 2 number list with x first and then y
    """
    pointlist=[]
    for i in range(distance):
        pointlist.append((start[0],start[1] +i+1))
    return pointlist

def go_down(start,distance):
    """
    start is a 2 number list with x first and then y
    """
    pointlist=[]
    for i in range(distance):
        pointlist.append((start[0],start[1] - i - 1))
    return pointlist

def go_right(start,distance):
    """
    start is a 2 number list with x first and then y
    """
    pointlist=[]
    for i in range(distance):
        pointlist.append((start[0] +i+1,start[1]))
    return pointlist

def go_left(start,distance):
    """
    start is a 2 number list with x first and then y
    """
    pointlist=[]
    for i in range(distance):
        pointlist.append((start[0] - i - 1,start[1]))
    return pointlist


def taxi_distance(point):
    """
    find the taxi distance from 0,0 of a poin you pass in
    """
    distance = abs(point[0]) +abs(point[1])
    return distance

with open("maininput.txt") as f:
    input_original = f.read()

print(input)
input_list = input_original.split()
input = ([input_list[0].split(','),input_list[1].split(',')])
#input = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']]
#input = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]
path =[[(0,0)],[(0,0)]]
for i, group in enumerate(input):
    for move in group:
        direction = move[0]
        distance = int(move[1:])
        start = path[i][-1]
        print(start)

        if direction == 'U':
            path[i] = path[i] + go_up(start,distance)
        if direction == 'R':
            path[i] = path[i] + go_right(start, distance)
        if direction == 'D':
            path[i] = path[i] + go_down(start,distance)
        if direction == 'L':
            path[i] = path[i] + go_left(start,distance)





lineone = set(path[0])
linetwo = set(path[1])

z = lineone.intersection(linetwo)
z.remove((0,0))

print('z', z)


# for i in z:
#     y = taxi_distance(tuple(i))
#     print(i,y)

#for result in z:
   # print(result)

best_result = 99999999999999999999999999999999999
for i in z:
    #print(i)
    count_one = 0
    for result in range(len(path[0])):
        if i == path[0][count_one]:
            #print(i, path[0][count_one] + 'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
            break
        else:
            #print(i,path[0][count_one])
            count_one += 1
    count_two = 0
    for result in range(len(path[1])):
        if i == path[1][count_two]:
            break
        else:
            count_two += 1
    if (count_one + count_two)<best_result:
        best_result = count_two + count_one
    print(i,count_one + count_two)
print(best_result)
