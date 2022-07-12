from sympy import N


def func(n):
    str_num = str(n)
    sum = n
    
    for i in str_num:
        sum += int(i)
        
    return sum

n_list = [i for i in range(1, 10000+1)]
sn_list = []

# for i in range(1, 10000+1):
#     num = i
#     nsn_list = []
    
#     while True:
#         if num >= 10000:
#             break
        
#         num = func(num)
#         nsn_list.append(num)
    
#     sn_list = list(set(sn_list) - set(nsn_list))
    
# sn_list.sort()

for i in n_list:
    for j in str(i):
        i += int(j)
    sn_list.append(i)
    
n_list = sorted(list(set(n_list) - set(sn_list)))

print(*n_list, sep='\n')


