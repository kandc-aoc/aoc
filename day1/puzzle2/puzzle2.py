# The regex
# r = re.findall('one|two|three|four|five|six|seven|eight|nine|\d', x)
# returns a list of all matches
# the first match can be retrieved by referencing r[0]
# and the last can be retrieved by referencing r[-1]
#

<<<<<<< HEAD
import re

def find_words(s):
    #print ('input:' + s)
    first='a'
    last='a'
    r = re.findall('one|two|three|four|five|six|seven|eight|nine|\d', s)
    first=r[0]
    last=r[-1]
    return first, last

with open('example_input.txt') as test:
    for line in test:
        find_words(line)
        print("first "+first+" last "+last)
       # grand_total=grand_total+int((find_first(line)+find_last(line)))
=======

dict = {'one': '1', 'two': '2', 'three': '3', 'four' : '4', 'five' : '5',
           'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9', '1' : '1', '2' : '2',
           '3' : '3', '4' : '4', '5' : '5', '6' : '6', '7' : '7', '8' : '8', '9' : '9'}

def combine_to_int(first, last):
    f = dict[first]
    l = dict[last]
    return int (f + l)
>>>>>>> 8ce8598b3db04b5cd75a34768c27e3dcd0d58c11
