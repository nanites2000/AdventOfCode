#23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,479,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19
# 0 1 2 3 4 5 6 7 8 9101112,13,141516,17,        ,23 ,                       ,36,     ,40,                     ,52, ,54 ,                                   ,73
busses = [23, 41, 37, 479, 13,17,29,373,19]
start= 1000417
for i in busses:
    mod = start % i
    print(mod, i, i - mod )
start = 32579483440
start = 100000000000000
start = 100000043322995
start = 211407173614266  #biger than this
#part 2
#start += 14 # set the start to a multiple of 23 the first bus
# while True:
#     if start % 23 == 0 and start % 41 == 13 and start % 37 == 17 and start % 479 == 23 and start % 13 == 10\
#             and start % 17 == 6 and start % 29 == 23 and start % 373 == 54 and start % 19 == 16:
#         print(start)
while True:
    #print('start' + str(start))
    if start % 479 == 23 and start % 23 == 0 and start % 41 == 13 \
            and start % 37 == 17 and start % 479 == 23 and start % 13 == 10:
        if start % 479 ==23:
            print(473,start)
        if start % 17 == 6:
            print(17777777777777777,start)
            if start % 29 == 23:
                print(29, start)
                if start % 373 == 54:
                    print(373, start)
                    if start % 19 == 16:
                        print(19, start)
    start +=1 #473
