input = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""

input = (input.split('\n'))
print(input)
input = [(i.strip()).split('=>') for i in input]
print(input)

for i in input
input = [(i.strip()).split(' ') for j in i]
print( input)