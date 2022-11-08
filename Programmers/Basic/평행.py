from itertools import combinations


def solution(dots):
    
    combi_l = list(combinations(dots, 2))
    inclination = []
    
    for i in combi_l:
        inclination.append((i[1][0]-i[0][0]) / (i[1][1]-i[0][1]))
    
    if len(inclination) == len(set(inclination)):
        return 0
    else:
        return 1
    