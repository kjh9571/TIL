from collections import Counter

def solution(s):
    
    string = list(s)
    cnt = Counter(string)
    ns = []
    
    for key, value in cnt.items():
        if value == 1:
            ns.append(key)
    
    return ''.join(sorted(ns))

# def solution(s):
#     answer = "".join(sorted([ch for ch in s if s.count(ch) == 1]))
#     return answer
