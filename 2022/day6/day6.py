
with open("input2.txt") as input:
    lines = input.readlines()

test_list = []
for index, letter in enumerate(lines[0]):

    if index in [0, 1, 2]:
        test_list.append(letter)
    else:

        if letter in test_list:
            test_list.append(letter)
            print(test_list)
            test_list.pop(0)
        else:

            if test_list.count(test_list[0]) > 1 or test_list.count(test_list[1]) > 1 or test_list.count(test_list[2]) > 1:
                test_list.append(letter)
                print(test_list)
                test_list.pop(0)
            else:
                print(f"index is {index}")
                print(test_list)
                break
