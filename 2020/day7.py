with open('day7_input.txt') as f:
    a = f.readlines()
bag_dict = {}
for row in a:
    name,baglist = row.split('contain')
    print(name, baglist)
    name = name.split(' bag')[0]
    bags = baglist.split(',')
    print(bags)
    for bag in bags:
        bag = bag.split('.')[0]
        bag = bag[3:]
        bag = bag.split(' bag')[0]
        print(bag)
        #bag_dict.update({name:[bag]})
        bag_dict.setdefault(bag, []).append(name)
print(bag_dict)

bagfinal = set(bag_dict['shiny gold'])

while True:
    for bag in bagfinal:
        try:
            bagfinal = bagfinal | set(bag_dict[bag])
        except:
            pass
        print(bagfinal)
        print(len(bagfinal))