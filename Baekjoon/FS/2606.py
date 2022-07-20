c = int(input())
n = int(input())
net = [[] for i in range(c+1)]
result = []

for i in range(n):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)
    
def search(idx):
    if net[idx] == []:
            return
    
    for i in net[idx]:
        if i in result:
            continue
        else:
            result.append(i) 
            search(i)
            
search(1)

result.remove(1)
print(len(result))