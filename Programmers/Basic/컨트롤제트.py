def solution(s):
    
    l = s.split(' ')
    stack = []
    
    for i in l:
        if i == 'Z':
            if not stack:
                continue
            else:
                stack.pop()
        else:
            stack.append(int(i))        
            
    return sum(stack)
