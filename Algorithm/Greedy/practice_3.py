n = int(input())
fears = list(map(int, input().split()))
fears.sort()
cnt = 0 # 현재 그룹에 포함된 모험가의 수
grp = 0 # 총 그룹의 수

for fear in fears: # 공포도를 낮은 것부터 하나씩 확인하며
    cnt += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if cnt >= fear: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        grp += 1 # 총 그룹의 수 증가시키기
        cnt = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(grp) # 총 그룹의 수 출력
        
