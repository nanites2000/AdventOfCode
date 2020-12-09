with open('day7_input.txt') as f:
    a = f.readlines()

a=[
'shiny gold bags contain 2 dark red bags.',
'dark red bags contain 2 dark orange bags.',
'dark orange bags contain 2 dark yellow bags.',
'dark yellow bags contain 2 dark green bags.',
'dark green bags contain 2 dark blue bags.',
'dark blue bags contain 2 dark violet bags.',
'dark violet bags contain no other bags.',

]
bag_dict = {}
for row in a:
    name,baglist = row.split('contain')
    #print(name, baglist)
    name = name.split(' bag')[0]
    bags = baglist.split(',')
    #print(bags)
    for bag in bags:
        bag = bag.split('.')[0]
        #print(bag)
        try:
            number = int(bag[1])
        except:
            break
        bag = bag[3:]

        bag = bag.split(' bag')[0]
        #print(bag)
        #bag_dict.update({name:[bag]})
        # the false in each entry keeps track if it has been loaded or not
        bag_dict.setdefault(name, {}).update({bag: {'number': number, 'already': False}})
print(bag_dict)
print(bag_dict['shiny gold'])

bagfinal = bag_dict['shiny gold']

# maybe do the same but keep track of the multiplier between bags and the total
while True:
    newbagfinal = {}
    for bag in bagfinal:
        #print(bag)
        if not bagfinal[bag]['already']:
            bagfinal[bag]['already'] = True
            print('bag')
            try:
                for name, data in bag_dict[bag].items():
                    if name in bagfinal.keys():
                        bagfinal[name]['number'] += data['number']
                    else:
                        newbagfinal.update({name: data})
            except:
                print('Passed on', bag)

    bagfinal.update(newbagfinal)
    # print(len(bagfinal.keys()))
    # sum=0
    # for i in bagfinal.values():
    #     sum += i['number']
    # print(sum)
    #i probably need recursion
    #153 is low

    #     newbags = bag_dict[bag[0]]
    #     print(newbags)
    #     bag[2] = True
    #
    #     for newbag in newbags:
    #         if newbag in bagfinal:
    #             #problem!!!!!! not  a dictionary change to one!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #             bagfinal[newbag][1] = bagfinal[newbag][1] + newbag[1]
    #         else:
    #              bagfinal.append(bag)
    #
    # print(bagfinal)
    #
