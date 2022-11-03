from itertools import combinations

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int((x+1)**0.5)+1):
            if x % i == 0:
                return False
    return True

def solution(nums): 
    cnt = 0
    
    for i in list(combinations(nums, 3)):
        if isPrime(sum(i)):
            cnt += 1
            
    return cnt