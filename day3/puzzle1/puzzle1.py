import regex as re

def locate_symbols(text):
    list_symbol=[]
    x =0
    y=0
    for line in text:
        line=line.strip()
        for char in line:
            if(re.search("[^.,\d]", char)):
                print(x,y,char)
                list_symbol.append([x,y,char])
            y=y+1
        y=0
        x=x+1
    return list_symbol

with open('example_input.txt') as test:
    symbol_list=locate_symbols(test)
    print(symbol_list)