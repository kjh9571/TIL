def solution(s):
    stack = []
    
    for i in s:
        if stack == []:
            stack.append(i)
            continue
            
        if i == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)
    
    if stack == []:
        return True
    else:
        return False