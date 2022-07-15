## 시간 초과된 내 알고리즘

# m = int(input())
# m_list = list(map(int,input().split()))
# n = int(input())
# n_list = list(map(int,input().split()))
# result = []

# m_list.sort()

# for i in n_list:
#     slice_list = m_list
    
#     while True:
        
#         m = m // 2
        
#         if slice_list == []:
#             result.append('0')
#             break
        
#         if i == slice_list[m]:
#             result.append('1')
#             break
#         elif i > slice_list[m]:
#             slice_list = slice_list[m+1:]
            
#         else:
#             slice_list = slice_list[:m]
        
# print(' '.join(result))

## set 이용 방법

# input()
# n = set(map(int, input().split()))
# input()
# m = list(map(int, input().split()))

# for i in m:
#     if i in n:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

n = int(input())
a = list(map(int, input().split()))
a.sort()

def binary_search(num):
    l = 0
    r = n-1
    while l <= r :
        mid = (l+r)//2
        if a[mid] == num :
            return 1
        elif a[mid] > num :
            r = mid - 1
            # 반 줄여주기 1
        else:
            l = mid + 1
            # 반 줄여주기 2
    return 0

input()
for num in list(map(int, input().split())):
    print(binary_search(num), end = ' ')