# n = int(input())
# m = []

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         m.append([i,j])

# L = list(map(str, input().split()))

# Right = [0, 1]
# Left = [0, -1]
# Up = [-1, 0]
# Down = [1, 0]
# goal = [1, 1]

# for i in L:
#     if i == 'R':
#         goal = [a+b for a,b in zip(goal,Right)]
#         dir = Right
#     elif i == 'L':
#         goal = [a+b for a,b in zip(goal,Left)]
#         dir = Left
#     elif i == 'U':
#         goal = [a+b for a,b in zip(goal,Up)]
#         dir = Up
#     else:
#         goal = [a+b for a,b in zip(goal,Down)]
#         dir = Down
#     if goal in m:
#         continue
#     else:
#         goal = [a-b for a,b in zip(goal,dir)]

# print(' '.join(map(str, goal)))

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x,y)