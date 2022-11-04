def solution(participant, completion):
    
    sum_hash = 0
    dict = {hash(name):name for name in participant}
    
    for i in participant:
        sum_hash += hash(i)
    
    for i in completion:
        sum_hash -= hash(i)
    
    return dict[sum_hash]