s = int(input())
sum = 0
cnt = 0
st = 1

while True:
    sum = sum + st

    if sum > s:
        break
    else:
        cnt += 1
        st += 1

print(cnt)