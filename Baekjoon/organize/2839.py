n = int(input())
val = n//5
res = 0

if n % 5 == 0:
    res = val
else:
    for i in range(val, 0, -1):
        n2 = n - (5*i)
        if n2 % 3 == 0:
                res = i + (n2//3)
                break

    if n % 3 == 0 and res == 0:
        res = n//3
    else:
        if res == 0:
            res = -1

print(res)