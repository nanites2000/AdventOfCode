with open('day4_input.txt') as f:
    a = f.readlines()
b = ['']
for line in a:
    if len(line) > 2:
        b[-1] = b[-1] + ' ' + line.strip()
    else:
        b.append('')

print(b)
count = 0
g= {}
for line in b:
    print(line)
    j = (line.split())
    g={}
    for i in j:
        key, value = i.split(':')
        g.update({key:value})
    #print (g)
    if line.count('byr') == 1 and line.count('iyr') == 1 and line.count('eyr') == 1 and line.count('hgt') == 1 and line.count('hcl') == 1 and line.count('ecl') == 1 and line.count('pid') == 1:
        index = 0
        for letter in g['hgt']:
            if letter.isnumeric():
                index += 1
            else:
                break
        hgt_num = g['hgt'][0:index]
        hgt_letters = g['hgt'][index:]

        passing = True
        for digit in g['hcl'][1:]:
            if not digit in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                passing = False

        pid_number = True
        try:
            int(g['pid'])
        except:
            pid_number = False
        #print(g['hcl'], passing)

       # print(hgt_num,hgt_letters)

        if (len(g['byr']) == 4) and (1920 <= int(g['byr']) <= 2002):
            if (len(g['iyr']) == 4) and (2010 <= int(g['iyr']) <= 2020):
                if (len(g['eyr']) == 4) and (2020 <= int(g['eyr']) <= 2030):
                    if (hgt_letters == 'in' and (59 <= int(hgt_num) <= 76)) or (hgt_letters == 'cm' and (150 <= int(hgt_num) <=193)):
                        if g['hcl'][0] == '#' and passing:
                            if g['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
                                if pid_number and len(g['pid']) == 9:
                                    count += 1
                                    print(count)

print(count)