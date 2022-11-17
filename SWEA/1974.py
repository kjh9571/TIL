case = int(input())
s = [1,2,3,4,5,6,7,8,9]
check = 0

for case in range(1, case+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # print(sudoku[0][0])

    # 가로 확인
    for i in sudoku:
        l = sorted(i)
        # print(i)
        if l != s:
            check += 1
            # print("horizon")
            break

    # 세로 확인
    vertical = []

    for i in range(9):
        for j in range(9):
            # print(j,i)
            # print(sudoku[j][i])
            vertical.append(sudoku[j][i])

        vertical.sort()
        # print(vertical)
        if vertical != s:
            check += 1
            # print("vertical")
            break
        else:
            vertical = []

    # 부분 확인
    point = [[0, 0], [0, 3], [0, 6],
            [3, 0], [3, 3], [3, 6],
            [6, 0], [6, 3], [6, 6]]
    part = []

    for i in point:
        start = i.copy()
        # print(i)
        for j in range(3):
            for k in range(3):
                part.append(sudoku[start[0]][start[1]])
                start[1] += 1
            start[0] += 1
            start[1] = i[1]
        # print(part)

        part.sort()
        if part != s:
            check += 1
            break
        else:
            part = []

    if check != 0:
        print(f'#{case} 0')
    else:
        print(f'#{case} 1')
        
    check = 0
