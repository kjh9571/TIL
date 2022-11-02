def solution(n, lost, reserve):
    
    reserve.sort()
    r = set(reserve) - set(lost)
    l = set(lost) - set(reserve)
    
    for i in r:
        if (i-1) in l:
            l.remove(i-1)
        elif (i+1) in l:
            l.remove(i+1)
    
    return n - len(l)