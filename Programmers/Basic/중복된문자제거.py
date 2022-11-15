def solution(my_string):
    answer = ''
    s = set([])
    
    for i in my_string:
        if i not in s:
            answer += i
        else:
            pass
        
        s.add(i)
    
    return answer

# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in answer:
#             answer+=i
#     return answer