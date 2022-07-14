cnt = 1

while True:
    l,p,v = map(int, input().split())

    if l == p == v == 0:
        break
    else:
        n = v // p + 1
        sum = 0

        for i in range(n):
            if v <= l:
                sum += v
            else:
                sum += l
                v -= p
                
        print(f'Case {cnt}: {sum}')
        
    cnt += 1 
            