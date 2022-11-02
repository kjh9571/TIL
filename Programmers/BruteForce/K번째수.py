def solution(array, commands):
    answer = []
    
    for i in commands:
        cut_arr = array[i[0]-1:i[1]]
        cut_arr.sort()
        answer.append(cut_arr[i[2]-1])
        
    return answer