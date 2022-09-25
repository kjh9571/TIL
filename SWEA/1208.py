case = 1

while case != 11:
    dump = int(input())
    height = list(map(int, input().split()))

    while True:
        if dump != 0:
            for i in range(len(height)):
                if height[i] == max(height):
                    height[i] = max(height) - 1

                    height[height.index(min(height))] += 1
                    dump -= 1
                    # print(height)
                    break
        else:
            print(f'#{case} {max(height) - min(height)}')
            break
    
    case += 1



