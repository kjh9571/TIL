n = int(input())
sqrt = n//2
pre_sqrt = 0

while True:
    if sqrt**2 == n:
        print(sqrt)
        break
    elif sqrt**2 > n:
        pre_sqrt = sqrt 
        sqrt //= 2
        continue
    else:
        sqrt = (sqrt + pre_sqrt) // 2