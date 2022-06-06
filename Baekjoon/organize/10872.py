#!/usr/bin/env python
# coding: utf-8

# In[8]:


n = int(input())
res = 1

while n != 0:
    res *= n
    n -= 1
    
print(res)


# In[10]:


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

