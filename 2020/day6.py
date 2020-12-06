with open('day6_input.txt') as f:
    a = f.readlines()

a.append('')
#Part1
seat_id_list = []
letters_results = []
letters_set = set()
for line in a:
    line = line.strip()
    if line:
        letters_set = letters_set | {char for char in line}
    else:
        letters_results.append(len(letters_set))
        letters_set = set()

print(sum(letters_results))


#part2
seat_id_list = []
letters_results = []
letters_set = set()
begun = False
for line in a:
    line = line.strip()
    if line:
        if not letters_set and begun == False:
            letters_set = letters_set | {char for char in line}
            begun = True
        else:
            letters_set = letters_set.intersection({char for char in line})
    else:
        letters_results.append(len(letters_set))
        letters_set = set()
        begun = False

print(sum(letters_results))

#3693 wrong