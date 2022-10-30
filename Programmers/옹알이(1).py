def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for i in range(len(babbling)):
        s = babbling[i]
        for j in can:
            if j in s:
                s = s.replace(j,' ',1)
                s = s.strip(' ')
                if s == '':
                    cnt += 1
                    break
            else:
                continue
    
    return cnt