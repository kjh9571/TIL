#!/usr/bin/env python
# coding: utf-8

# In[77]:


def func(x):
    count = 0

    if x < 100:
        return x
    else:
        while x != 100:
            check = 1
            d = 0
            x = str(x)
            for i in range(len(x)-1):
                d = int(x[1]) - int(x[0])
                dif = int(x[i+1]) - int(x[i])
                if d == dif:
                    pass
                else:
                    check = 0
                    break
                
            if check == 1:
                count += 1
            x = int(x)
            x -= 1
    
        return 99 + count          
    
x = int(input())
print(func(x))


# In[74]:


func(100)


# In[ ]:




