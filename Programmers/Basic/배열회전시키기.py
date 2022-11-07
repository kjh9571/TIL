from collections import deque

def solution(numbers, direction):
    deq = deque(numbers)
    
    if direction == 'right':
        item = deq.pop()
        deq.appendleft(item)
    else:
        item = deq.popleft()
        deq.append(item)
    
    return list(deq)