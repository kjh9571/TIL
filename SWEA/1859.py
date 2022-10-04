t = int(input())

for i in range(1, t+1):
    n = int(input())
    price = list(map(int, input().split()))
    max_p = max(price)
    profit = 0

    if price[0] == max(price):
        print(f'#{i} 0')
        continue
    else:
        for j in range(len(price)):
            if price[j] == max_p:
                if price[j+1:] != []:
                    max_p = max(price[j+1:])
            else:
                profit += max_p - price[j]
        
        print(f'#{i} {profit}')