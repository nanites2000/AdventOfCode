
with open("input.txt") as input:
    lines = input.readlines()

test_list = []
for index, letter in enumerate(lines[0]):

    if index in range(13):
        test_list.append(letter)
        print(test_list)
    else:

        if letter in test_list:
            test_list.append(letter)
            print(test_list)
            test_list.pop(0)
        else:
            found = False
            for picked in test_list:
                if test_list.count(picked) > 1:
                    found = True
            if found:
                test_list.append(letter)
                print(test_list)
                test_list.pop(0)
            else:
                print(test_list)
                print(f"index is {index+ 1}")
                break
