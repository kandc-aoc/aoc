import re

import regex

with open('example_input.txt') as test:
    for line in test:
        breakup = [j for i in line.split(':') for j in i.split(';')]
        print(line,breakup)

