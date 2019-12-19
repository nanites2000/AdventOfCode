import math
def repeat(place,pattern, length):
    """
    pass a list of numbers as pattern
    pass the number representing the digit
    length is the int that matches how long the resulting string should be
    """
    output = []

    for j in pattern:
        for i in range(place):
            output.append(j)
    multiples = math.floor(length / len(pattern))+1
    result = output*multiples

    return result[1:length+1]

def mult_add(input, full_pattern):
    """
    both inputs are a list of ints
    they will be multiplied togehter and then all added
    the ones digit will be returned from the result of the sum

    """

    mult =[a*b for a,b in zip(input, full_pattern)]
    print(mult)
    mult_sum = sum(mult)
    print('mult',mult_sum)
    convert = convert_num_to_list(mult_sum)
    print('convert',convert)
    return(convert[-1:][0])

def convert_num_to_list(number):
    """
    takes a int and breaks
    """
    str_num = list(str(abs(number)))
    int_num = [int(i) for i in str_num]
    return(int_num)

if __name__ == "__main__":
    #input = 80871224585914546619083218645595
    #input = 19617804207202209144916044189917
    input = 59790132880344516900093091154955597199863490073342910249565395038806135885706290664499164028251508292041959926849162473699550018653393834944216172810195882161876866188294352485183178740261279280213486011018791012560046012995409807741782162189252951939029564062935408459914894373210511494699108265315264830173403743547300700976944780004513514866386570658448247527151658945604790687693036691590606045331434271899594734825392560698221510565391059565109571638751133487824774572142934078485772422422132834305704887084146829228294925039109858598295988853017494057928948890390543290199918610303090142501490713145935617325806587528883833726972378426243439037
    input = convert_num_to_list(input)
    print(input)
    print('the output length :::::::::::::', len(input))
    new_input = []
    for i in range(100):
        print(len(input))
        for j in range(len(input)):
            pattern = repeat(j+1, [0, 1, 0, -1], len(input))

            result = mult_add(input,pattern)
            new_input.append(result)
        input = new_input
        print(input)
        new_input = []
    print(input)



    # for k in range(100):
    #
    # repeat(1, [0,1,0,-1],10)