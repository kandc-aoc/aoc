
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

GrandTotal = 0
first_digit=0
last_digit=0

=======
#Iterates over the input file and for each
#line (containing a string) call the find_first
#and find_lass functions, combine their return
#values and add them to running total


with open('example_input.txt') as test:
    for line in test:
        first_digit=find_first(line)
        last_digit=find_last(line))
        
    