
#Starts looking at the start of the
#provided string and finds and returns
#the first digit
def find_first(s):
    #print ('input:' + s)
    j=0
    x='a'
    while (not x.isdigit()):
        x = s[j]
        #print ("s at j where j = 0 " + s[j])
        #print ("x updated to s[j] " + x)
        j = j + 1
    return x

#Starts looking at the end of the
#provided string and finds and returns
#the first digit
def find_last(s):
    #print ('input:' + s)
    j=len(s)-1
    x='a'
    while (not x.isdigit()):
        x = s[j]
        #print ("s at j where j = 0 " + s[j])
        #print ("x updated to s[j] " + x)
        j = j -1
    return x

#Iterates over the input file and for each
#line (containing a string) call the find_first
#and find_lass functions, combine their return
#values and add them to running total

total = 0

with open('example_input.txt') as test:
    s = ''
    for line in test:
        print(find_first(line))
        print(find_last(line))
    