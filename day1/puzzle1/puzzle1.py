
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

grand_total = 0


#Iterates over the input file and for each
#line (containing a string) call the find_first
#and find_lass functions, combine their return
#values and add them to running total


with open('puzzle_input_2.txt') as test:
    for line in test:
        #print(find_first(line)+find_last(line))
        grand_total=grand_total+int((find_first(line)+find_last(line)))
        
        
        
print(grand_total)    