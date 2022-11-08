# def fact(n):
#     if n == 1:
#         return 1
    
#     res = n * fact(n-1)
#     return res

from math import factorial as fact

def solution(n):
    num = 1
    
    while True:
        res = fact(num)
        
        if fact(num+1) > n:
            break
        else:
            num += 1
            
    return num