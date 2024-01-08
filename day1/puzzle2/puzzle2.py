# The regex
# r = re.findall('one|two|three|four|five|six|seven|eight|nine|\d', x)
# returns a list of all matches
# the first match can be retrieved by referencing r[0]
# and the last can be retrieved by referencing r[-1]
#

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

