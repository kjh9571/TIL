cnt = 0
def solution(numbers, target):
    def add(res, numbers, idx):
        global cnt
        if idx == len(numbers):
            if res == target:
                cnt += 1
                return
            else:
                return
        else:
            res1 = res + numbers[idx]
            res2 = res - numbers[idx]
            add(res1, numbers, idx + 1)
            add(res2, numbers, idx + 1)
        
    add(0, numbers, 0)
    
    return cnt