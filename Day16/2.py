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
    #print(mult)
    mult_sum = sum(mult)
    #print('mult',mult_sum)
    convert = convert_num_to_list(mult_sum)
    #print('convert',convert)
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
    #since input has length 650 two groups of it divide into the 4 digit pattern so you do not have to calculate the rest
    input = 5979013288034451690009309115495559719986349007334291024956539503880613588570629066449916402825150829204195992684916247369955001865339383494421617281019588216187686618829435248518317874026127928021348601101879101256004601299540980774178216218925295193902956406293540845991489437321051149469910826531526483017340374354730070097694478000451351486638657065844824752715165894560479068769303669159060604533143427189959473482539256069822151056539105956510957163875113348782477457214293407848577242242213283430570488708414682922829492503910985859829598885301749405792894889039054329019991861030309014250149071314593561732580658752888383372697237842624343903759790132880344516900093091154955597199863490073342910249565395038806135885706290664499164028251508292041959926849162473699550018653393834944216172810195882161876866188294352485183178740261279280213486011018791012560046012995409807741782162189252951939029564062935408459914894373210511494699108265315264830173403743547300700976944780004513514866386570658448247527151658945604790687693036691590606045331434271899594734825392560698221510565391059565109571638751133487824774572142934078485772422422132834305704887084146829228294925039109858598295988853017494057928948890390543290199918610303090142501490713145935617325806587528883833726972378426243439037

    input = convert_num_to_list(input)
    first_seven = input[0:7]
    print(first_seven)
    number = 0
    for index, i in enumerate(first_seven):
        number += i*10**(6-index)
        print(number)
    print(number)
    #full_number = ''.join(numbers)
    #print(full_number)
    #print(input)
    #print('the output length :::::::::::::', len(input))
    new_input = []
    for i in range(100):
        #print(len(input))
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