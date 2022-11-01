def solution(arr):
    answer = []
    for i in arr:
        if answer == [] or answer[-1] != i:
            answer.append(i)
        else:
            if answer[-1] == i:
                continue
        
    return answer

# def solution(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a