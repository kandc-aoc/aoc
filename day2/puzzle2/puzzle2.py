import regex as re

grand_total=0
game = 0

s = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

#regex checking function
#EDIT to output the max value for each colour cubed
def max_color(line,color):
    p = '(\d+)\s'+color
    cp = re.compile(p)
    m = cp.findall(line)
    colormax=0
    for match in m:
        if int(match) > colormax:
                colormax=int(match)
    return colormax


#print(max_color(s,'blue'))

#edit to add grand total without skipping games
with open('puzzle_input2.txt') as test:
    for line in test:

    print (grand_total)

