#!/usr/bin/env python
# coding: utf-8

# # 2072

# In[ ]:


case = int(input())
newl = []

while case != 0:
    nl = list(map(int, input().split()))
    s = 0

    for i in nl:
        if i % 2 != 0:
            s += i
    newl.append(s)
    case -= 1
    
for i in newl:
    print(f'#{newl.index(i) + 1} {i}')


# # 1204

# In[ ]:


case = int(input())
result = []

while case != 0:
    num = int(input())
    nl = list(map(int, input().split()))
    nd = {i : 0 for i in nl}
    
    for i in nl:
        if i in nd:
            nd[i] += 1
    result.append(max(nd,key=nd.get))
    case -= 1
    
for i in result:
    print(f'#{result.index(i) + 1} {i}') 

