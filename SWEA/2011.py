t = int(input())
idx = 1
 
while t >= idx:
    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]
 
    start = [0, 0]
    check = 0
    sum_l = []
 
    while True:
 
        #print(f'start : {fly[start[0]][start[1]]}')
        # print(start)
 
        ns = start.copy()
        nm = 0
        sum = 0
        while True:
 
            #print(fly[ns[0]][ns[1]])
            sum += fly[ns[0]][ns[1]]
 
            #print(start, ns)
            if (ns[1]-start[1])+1 == m:
                ns[0] += 1
                ns[1] = start[1]
                nm += 1
            else:
                ns[1] += 1
 
            #print(ns)
 
            if nm == m:
                sum_l.append(sum)
                break
 
        if start[1] == len(fly[0]) - m:
            start[0] += 1
            start[1] = 0
        else:
            start[1] += 1
 
        if check == 1:
            break
 
        if start == [len(fly)-m, len(fly[0])-m]:
            #print(fly[start[0]][start[1]])
            check += 1
 
    print(f'#{idx} {max(sum_l)}')
    idx += 1
