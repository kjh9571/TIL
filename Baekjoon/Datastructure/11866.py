from collections import deque

n, k = map(int, input().split())

circle = deque([i for i in range(1, n+1)])
josephus = deque([])

while True:
    if n == 1:
        josephus = deque([1])
        break
    
    for i in range(k):
        if i == k-1:
            josephus.append(circle.popleft())
        else:
            circle.append(circle.popleft())
    
    if len(josephus) == n:
        break

print("<", end='')
for i in range(len(josephus)-1):
    print(f'{josephus[i]}', end=', ')
print(f'{josephus[-1]}', end = '')
print(">")
