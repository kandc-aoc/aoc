# The regex
# r = re.findall('one|two|three|four|five|six|seven|eight|nine|\d', x)
# returns a list of all matches
# the first match can be retrieved by referencing r[0]
# and the last can be retrieved by referencing r[-1]
#

import re
import csv

grand_total=0

dict  = {'one': '1', 'two': '2', 'three': '3', 'four' : '4', 'five' : '5',
           'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9', '1' : '1', '2' : '2',
           '3' : '3', '4' : '4', '5' : '5', '6' : '6', '7' : '7', '8' : '8', '9' : '9'}


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

def combine_to_int(firstnum, lastnum):
    f = dict[firstnum]
    l = dict[lastnum]
    return int (f + l)

count=0
resdict={}

with open('puzzle_input.txt') as test:
    for line in test:
        count = count+1
        firstnum,lastnum=find_words(line)
        result=combine_to_int(firstnum,lastnum)
        #print("first "+firstnum+" last "+lastnum)
        resdict[line.strip()]=result
        grand_total=grand_total+result
    print (grand_total)
    print(count)

with open('res.csv','w') as f:
    w = csv.writer(f)
    w.writerows(resdict.items())



