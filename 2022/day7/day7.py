
with open("input.txt") as input:
    lines = input.readlines()

class Directory:
    def __init__(self, name):
        self.__name__ = name
        self.children = []
        self.value = 0
input = "/"
all_directories = {
input:{
'children':['qcznqph', 'qtbprrq'],
'size':4000
},
"qcznqph":{
 'children':['lnj',  'mtr', 'mznnlph']
}
}

print(all_directories)

for child in all_directories['qcznqph']['children']:
    print(child)
# all_dirs = {}
# current_path = []
# for line in lines:
#     size = 0
#     a = line.split()
#     if len(a) == 3:
#
#     elif a[0] == "$":
#         pass
#     elif a[0] == "dir":
#         print("sub dir")
#     else:
#         size = a[0]
#     print(size)
