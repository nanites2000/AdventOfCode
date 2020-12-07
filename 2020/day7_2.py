with open('day7_input.txt') as f:
    a = f.readlines()
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
        bag_dict.setdefault(name, {}).update({bag:{'number':number,'already':False}})
print(bag_dict)
print(bag_dict['shiny gold'])

bagfinal = bag_dict['shiny gold']


# for bag in bagfinal:
#     if not bag[2]:
#         newbags = bag_dict[bag[0]]
#         print(newbags)
#         bag[2] = True
#
#         for newbag in newbags:
#             if newbag in bagfinal:
#                 #problem!!!!!! not  a dictionary change to one!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                 bagfinal[newbag][1] = bagfinal[newbag][1] + newbag[1]
#             else:
#                  bagfinal.append(bag)
#
#     print(bagfinal)

