
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


with open('example_input.txt') as test:
    for line in test:
        print(find_first(line))
        print(find_last(line))
    