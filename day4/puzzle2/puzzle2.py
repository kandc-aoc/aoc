from functools import reduce

def file_len(file_name):
    with open(file_name, 'r') as fp:
        num_lines = sum(1 for line in fp)
        return num_lines


def calculate_score(file_name):
    with open(file_name) as file:
        repeats=[1 for i in range(file_len(file_name))]
        l=0
        for line in file:
            l+=1
            points=0
            halves = line.split("|")
            first_half = halves[0].split()
            second_half = halves[1].split()
            for i in range(2, len(first_half)):
                for j in range(len(second_half)):
                    if first_half[i] == second_half[j]:
                        points=points+1
            a=repeats[l-1]
            for i in range(l, l+points):
                repeats[i]+=a
    return repeats

print(reduce(lambda x, y: x+y, calculate_score("puzzle_input.txt")))

