def solution(n, words):
    cycle = 1
    cnt = 1
    set_words = []
    
    for i in range(len(words)):
        if set_words == []:
            set_words.append(words[i])
            cnt += 1
            continue
        
        if words[i] in set(set_words) or words[i-1][-1] != words[i][0]:
            return [cnt, cycle]
        else:
            set_words.append(words[i])
        
        if cnt == n:
            cnt = 1
            cycle += 1
        else:
            cnt += 1
    
    return [0,0]

# def solution(n, words):
#     for p in range(1, len(words)):
#         if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
#     else:
#         return [0,0]