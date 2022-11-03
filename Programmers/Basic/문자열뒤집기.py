def solution(my_string):
    rev = ''
    
    for i in range(len(my_string)-1, -1, -1):
        rev = rev + my_string[i]
    
    return rev

# def solution(my_string):
#     return my_string[::-1]