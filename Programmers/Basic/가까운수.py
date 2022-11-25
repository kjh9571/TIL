def solution(array, n):
    
    array = list(set(array))
    
    if n in array:
        return n
    
    array.append(n)
    array.sort()
    
    # 맨 앞, 맨 뒤에 n이 있을 경우
    if array[-1] == n:
        return array[-2]
    
    if array[0] == n:
        return array[1]
    
    # list 중간에 n이 있는 경우
    left = n - array[array.index(n)-1]
    right = array[array.index(n)+1] - n
    
    if left > right:
        return array[array.index(n)+1]
    else:
        return array[array.index(n)-1]

# def solution(array, n):
#     array.sort(key = lambda x : (abs(x-n), x-n))
#     print(array)
#     answer = array[0]
#     return answer
