import regex as re

with open('example_input.txt') as test:
    for line in test:
        breakup = [j for i in line.split(':') for j in i.split(';')]
        print(line,breakup)


s = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

#regex checking function
def is_possible(line, color, total):
    p = '(\d+)\s+'+color
    cp = re.compile(p)
    m = cp.findall(line)
    for match in m:
        if int(match) > total:
            return False
    return True


print(is_possible(s, 'blue', 14))


