# The regex
# r = re.findall('one|two|three|four|five|six|seven|eight|nine|\d', x)
# returns a list of all matches
# the first match can be retrieved by referencing r[0]
# and the last can be retrieved by referencing r[-1]
#

import re

def find_words(s):
    #print ('input:' + s)
    firstnum='a'
    lastnum='a'
    #print(firstnum)
    r = re.findall('one|two|three|four|five|six|seven|eight|nine|\d', s)
    #print(r)
    firstnum=r[0]
    lastnum=r[-1]
    return firstnum, lastnum

with open('example_input.txt') as test:
    for line in test:
        firstnum,lastnum=find_words(line)
        #print("first "+firstnum+" last "+lastnum)
       # grand_total=grand_total+int((find_first(line)+find_last(line)))


dict = {'one': '1', 'two': '2', 'three': '3', 'four' : '4', 'five' : '5',
           'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9', '1' : '1', '2' : '2',
           '3' : '3', '4' : '4', '5' : '5', '6' : '6', '7' : '7', '8' : '8', '9' : '9'}

def combine_to_int(first, last):
    f = dict[first]
    l = dict[last]
    return int (f + l)


