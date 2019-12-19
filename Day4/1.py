import math
min = 347312
max = 805915


def split_num(value):
    result = []
    for i in range(5,-1,-1):
        divisor = 10**i
        digit = (math.floor(value/divisor))
        result.append(digit)
        value -= divisor * digit
    return(result)


total = 0

for i in range(min,max+1):
    digits = (split_num(i))
    fail = False
    equal = False
    for j in range(len(digits)-1):
        if digits[j]>digits[j+1]:
            #print('fail', digits)
            fail = True
        else:
            pass

        if digits[j]==digits[j+1]:
            equal = True
            print(digits)
        else:
            pass

    if (not fail) and equal:
       #print(digits)
        total += 1
print(total)













