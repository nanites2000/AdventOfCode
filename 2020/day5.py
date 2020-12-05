with open('day5_input.txt') as f:
    a = f.readlines()

#Part1
seat_id_list = []
for line in a:
    #find row number
    row_binary_string = line[0:7].replace('B', '1').replace('F', '0')
    row = (int(row_binary_string, 2))
    #find seat number
    seat_binary_string = line[7:10].replace('R', '1').replace('L', '0')
    seat = (int(seat_binary_string, 2))
    #calculate seatID
    seat_id_list.append(row * 8 + seat)
print(max(seat_id_list))

#part 2
seats = set(range(78, 960))
taken = set()
for line in a:
    row_binary_string = line[0:7].replace('B', '1').replace('F', '0')
    seat_binary_string = line[7:10].replace('R', '1').replace('L', '0')
    full_binary = int(row_binary_string + seat_binary_string, 2)
    taken.add(full_binary)

print(seats.difference(taken))
