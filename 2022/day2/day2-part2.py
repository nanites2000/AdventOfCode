
with open("input.txt") as input:
    lines = input.readlines()


def battle(first, second):
    special_sum = first + first


    mod_value = special_sum % 3
    print(special_sum, mod_value)
    if mod_value == 0:
        return 3  # Draw
    elif mod_value == 1:
        return 0  # lose
    elif mod_value == 2:
        return 6  # win
    else:
        return "Invalid numbers"


def convert(letter):
    if letter in ['A', 'X']:
        shape = 0  # Rock
    elif letter in ['B', 'Y']:
        shape = 1  # Paper
    else:
        shape = 2  # Scissors
    return shape



total_score = 0
for line in lines:
    first, second = line.split()
    first = convert(first)
    second = convert(second)
    result = battle(first, second)
    total_score += result  # the result of the battle
    total_score += second + 1 # to add the value from the shape thrown

print(f"Total Sum of Results: {total_score}")