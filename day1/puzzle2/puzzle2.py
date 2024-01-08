# The regex
# r = re.findall('one|two|three|four|five|six|seven|eight|nine|\d', x)
# returns a list of all matches
# the first match can be retrieved by referencing r[0]
# and the last can be retrieved by referencing r[-1]
#

import regex as re
import csv

#line_count=0

grand_total=0

dict  = {'one': '1', 'two': '2', 'three': '3', 'four' : '4', 'five' : '5',
           'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9', '1' : '1', '2' : '2',
           '3' : '3', '4' : '4', '5' : '5', '6' : '6', '7' : '7', '8' : '8', '9' : '9'}


def find_words(s):
    #print ('input:' + s)
    #print(firstnum)
    r = re.findall('one|two|three|four|five|six|seven|eight|nine|\d', s, overlapped=True)
    #print(r)
    firstnum=r[0]
    lastnum=r[-1]
    return firstnum, lastnum

def combine_to_int(firstnum, lastnum):
    f = dict[firstnum]
    l = dict[lastnum]
    return int (f + l)


with open('puzzle_input.txt') as test:
    for line in test:
        firstnum,lastnum=find_words(line)
        result=combine_to_int(firstnum,lastnum)
        #print("first "+firstnum+" last "+lastnum)
        grand_total=grand_total+result
    print (grand_total)







