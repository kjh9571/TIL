def solution(my_string, num1, num2):
    
    s = ''
    
    for i in range(len(my_string)):
        if i == num1:
            s += my_string[num2]
        elif i == num2:
            s += my_string[num1]
        else:
            s += my_string[i]
    
    return s

# def solution(my_string, num1, num2):
#     s = list(my_string)
#     s[num1],s[num2] = s[num2],s[num1]
#     return ''.join(s)
