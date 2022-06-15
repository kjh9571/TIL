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


# # 2071

# In[9]:


case = int(input())
res = []

while case != 0:
    nl = list(map(int, input().split()))
    avg = (sum(nl)) / len(nl)
    res.append(int(round(avg, 0)))
    case -= 1
    
for i in range(len(res)):
    print(f'#{i+1} {res[i]}')


# # 2070

# In[ ]:


case = int(input())
res = []

while case != 0:
    a, b = map(int, input().split())
    if a > b:
        res.append('>')
    elif a < b:
        res.append('<')
    else:
        res.append('=')
        

for i in range(1, len(res)+1):
    print(f'#{i} {res[i]}')


# # 1206

# In[15]:


cl = []

while True:
    length = int(input())
    hl = list(map(int,input().split()))
    count = 0

    for i in range(len(hl)):
        if hl[i] == 0:
            continue
        else:
            if (hl[i] > hl[i-1]) and (hl[i] > hl[i-2]) and (hl[i] > hl[i+1]) and (hl[i] > hl[i+2]):
                nl = [hl[i-2], hl[i-1], hl[i+1], hl[i+2]]
                count += hl[i] - max(nl)

    cl.append(count)
    
    if len(cl) == 10:
        break

for i in range(len(cl)):
    print(f'#{i+1} {cl[i]}')

