import regex as re

grand_total=0
game = 0

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

with open('example_input.txt') as test:
    for line in test:
        game=game+1
        if (is_possible(line,'blue',14) & is_possible(line,'red',12) & is_possible(line,'green',13)):
            grand_total=grand_total+game
    print (grand_total)

