def solution(n):
    
    res = set([])
    num = n
    
    while True:
        for i in range(2, num+1):
            if num % i == 0:
                res.add(i)
                num = num // i
                break
                
        if num == 1:
            break
    
    return sorted(list(res))

# def solution(n):
#     answer = []
#     d = 2
#     while d <= n:
#         if n % d == 0:
#             n /= d
#             if d not in answer:
#                 answer.append(d)
#         else:
#             d += 1
            
#     return answer
