from functools import reduce

def collect_numbers(file):
    numbers = []
    with open(file) as input:
        x = 0
        for line in input:
            number_data = []
            y = 0
            str_num = ''
            num_len = 0
            for char in line:
                if char.isdigit():
                    str_num += char
                    num_len += 1
                    if num_len == 1:
                        number_data.append(x)
                        number_data.append(y)
                else:
                    if num_len > 0:
                        number_data.append(str_num)
                        number_data.append(num_len)
                        numbers.append(number_data)
                        number_data = []
                    num_len = 0
                    str_num = ''
                y = y + 1
            x = x + 1
    return numbers

def collect_symbols(file):
    symbols = []
    #py error Python version 3.8 does not support parenthesized context expressions
    with open(file) as input:
        x = 0
        for line in input:
            symbol_data = []
            y = 0
            for char in line.strip():
                if char=="*":
                        symbol_data.append(char)
                        symbol_data.append(x)
                        symbol_data.append(y)
                        symbols.append(symbol_data)
                        symbol_data=[]
                y = y + 1
            x = x + 1
    return symbols

def gear_parts(number_list, symbol_list):
    gear_parts=[]
    for number_data in number_list:
        x_start = number_data[0]-1
        x_end = number_data[0]+2
        y_start = number_data[1]-1
        y_end = number_data[1]+number_data[3]+1
        #print ('loop set up', x_start, x_end, y_start, y_end)
        for symbol in symbol_list:
            for x in range(x_start, x_end):
                for y in range(y_start, y_end):
                    #print(x, y, symbol[1], symbol[2], number_data[2])
                    if x==symbol[1] and y==symbol[2]:
                        #print('MATCH', x, y, number_data[2])
                        symbol.append(int(number_data[2]))
    return symbol_list






#parts = part_nums(collect_numbers('example_input.txt'), collect_symbols('example_input.txt'))
#print(reduce(lambda x, y: x+y, parts))


gears = gear_parts(collect_numbers('puzzle_input_2.txt'), collect_symbols('puzzle_input_2.txt'))
total=0
for gear in gears:
    if len(gear)==5:
        total = total + (gear[3]*gear[4])

print(total)
