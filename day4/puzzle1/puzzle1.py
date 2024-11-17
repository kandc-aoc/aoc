
from functools import reduce

def get_points(score):
    if score == 0:
        return 0
    return pow(2, (score-1))



def calculate_score(file_name):
    with open(file_name) as file:
        line_total=[]
        for line in file:
            points=0
            halves = line.split("|")
            first_half = halves[0].split()
            second_half = halves[1].split()
            for i in range(2, len(first_half)):
                for j in range(len(second_half)):
                    if first_half[i] == second_half[j]:
                        points=points+1
            line_total.append(get_points(points))
    return line_total

print (reduce(lambda x, y: x+y, calculate_score('puzzle_input_2.txt')))
