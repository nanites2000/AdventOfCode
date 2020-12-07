with open('day6_input.txt') as f:
    a = f.readlines()
b = ['']
for line in a:
    if len(line.strip()) > 0:
        b[-1] = b[-1] + line.strip()
    else:
        b.append('')
print(b)
couint = 0
answer  = []
for row in b:
    answer.append(len(set({i for i in row})))
print(sum(answer))