# from collections import deque

# n, k = map(int, input().split())

# man_queue = deque([i for i in range(1,n+1)])
# josephus = []
    
# while True:
    
#     if n == 1:
#         josephus.append(1)
#         break
    
#     for i in range(len(man_queue)):
#         if i != k-1:
#             man_queue.append(man_queue[i])
#         else:
#             break
    
#     # print(man_queue)
#     # print(man_queue[2])
#     josephus.append(man_queue[k-1])
#     for i in range(k):
#         man_queue.popleft()
    
#     # print(man_queue)
    
#     if len(josephus)==n-1:
#         josephus.append(man_queue[0])
#         break

# print("<", end='')

# for i in range(len(josephus)-1):
#     print(f'{josephus[i]}', end=', ')

# print(f'{josephus[-1]}', end='')
# print(">")

from collections import deque

n, k = map(int, input().split())

circle = deque([i for i in range(1, n+1)])
josephus = deque([])

# print(f'init_circle : {circle}')

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
