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
with open('puzzle_input.txt') as test:
    grand_total = 0
    for line in test:
        total = max_color(line, 'blue')*max_color(line, 'red')*max_color(line,'green')
        grand_total += total
    print (grand_total)

