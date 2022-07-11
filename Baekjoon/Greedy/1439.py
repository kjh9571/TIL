# s = input()

# zero = []
# one = []
# zero_idx = 0 
# one_idx = 0

# for i in range(len(s)):
#     if s[i] == '0':
#         if i == 0:
#             zero.append([])
#             zero[zero_idx].append(s[i])
#         else:
#             if s[i-1] == '1':
#                 zero.append([])
#                 if len(zero) == 1:
#                     pass
#                 else:
#                     zero_idx += 1
#                 zero[zero_idx].append(s[i])
#             else:
#                 zero[zero_idx].append(s[i])
#     elif s[i] == '1':
#         if i == 0:
#             one.append([])
#             one[one_idx].append(s[i])
#         else:
#             if s[i-1] == '0':
#                 one.append([])
#                 if len(one) == 1:
#                     pass
#                 else:
#                     one_idx += 1
#                 one[one_idx].append(s[i])
#             else:
#                 one[one_idx].append(s[i])
        
# if len(zero) < len(one):
#     print(len(zero))
# else:
#     print(len(one))

s = input()
change = 0
std = ''

for i in s:
    if i != std:
        change += 1
        std = i

print(change//2)
