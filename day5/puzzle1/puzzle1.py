



headings = ['seed-to-soil map:', 'soil-to-fertilizer map:',
            'fertilizer-to-water map:', 'water-to-light map:',
            'light-to-temperature map:', 'temperature-to-humidity map:',
            'humidity-to-location map:']
#test comment
def get_next_input(input, des_base, src_base, range):
    if input >= src_base and input <= src_base+range:
        return des_base + input-src_base
    else:
        return input

def get_des_src_range(file_name, heading):
    add=False
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            if line.strip() == '':
                add=False
            if (add):
                res = [eval(i) for i in line.strip().split()]
                data.append(res)
            if line.strip() == heading.strip():
                add=True
    return data

print(get_des_src_range('example_input.txt', headings[0]))




inp=79
inp=get_next_input(inp,50,98,2)
print(inp)
inp=get_next_input(inp,52,50,48)
print(inp)



