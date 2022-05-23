#!/usr/bin/env python
# coding: utf-8

# # 10878

# In[19]:


ul = 0
def fib(x):
    global ul
    print(ul * '____' + '"재귀함수가 뭔가요?"')
    if x == 0:
        print(ul * '____' + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        ul += 1
    elif x != 0:
        print(ul * '____' + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(ul * '____' + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(ul * '____' + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        ul += 1
        fib(x-1)
    ul -= 1
    print(ul * '____' + '라고 답변하였지.')

n = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
fib(n)


# # 2447

# In[53]:


c = int(input())
nl = list(map(int, input().split()))
check = 0
count = 0

for i in nl:
    for j in range(1,1000+1):
        if i % j == 0:
            check += 1
    if check == 2:
        count += 1
    check = 0

print(count)


# # 2581

# In[9]:


st = int(input())
ed = int(input())
pnl = []

while st <= ed:
    count = 0
    
    for i in range(1,st+1):
        if st % i == 0:
            count += 1
            
    if count == 2:
        pnl.append(st)
    
    st += 1

if not pnl:
    print(-1)
else:
    print(sum(pnl))
    print(min(pnl))


# # 11653

# In[15]:


N = n = int(input())

while N != 1:
    for i in range(2,n+1):
        if N % i == 0:
            print(i)
            N //= i
            break


# In[18]:


## 11653 숏코딩
N=int(input())
a=2

while N>1:
    if N%a: # N % a의 값이 0이 아니면 들어가는 조건문
        a+=1
    else:
        print(a)
        N/=a


# # 1929

# In[9]:


def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int((x+1)**0.5)+1):
            if x % i == 0:
                return False
                
    return True
        
st, ed = map(int, input().split())

for i in range(st, ed + 1):
    if isPrime(i):
        print(i)

