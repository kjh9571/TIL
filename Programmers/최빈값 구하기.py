from collections import Counter


def solution(array):
    cnt = Counter(array)
    mc_num = cnt.most_common(1)[0][0]
    mc_cnt = cnt.most_common(1)[0][1]
    
    for i in range(len(cnt.most_common())):
        if i == 0:
            continue
        elif cnt.most_common()[i][1] == mc_cnt:
            return -1
        else:
            pass
            
    return mc_num