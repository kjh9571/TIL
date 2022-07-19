n = int(input())
numpad = [(list(map(int, input().split()))) for i in range(n)]
graph = [[0 for i in range(n)] for i in range(n)]
dx = [0, 1]
dy = [1, 0]
# print(numpad)
# print(numpad[n-1][n-1])

def jelly(x, y):
    num = numpad[x][y]
    
    if num == -1:
        print("HaruHaru")
        exit(0)
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        for i in range(2):
            nx = x + num * dx[i]
            ny = y + num * dy[i]
        
            if nx >= n or ny >= n:
                continue
            else:
                jelly(nx, ny)
            
    return "Hing"

print(jelly(0,0))