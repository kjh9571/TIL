def solution(my_string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    res = ''
    
    for i in range(len(my_string)):
        if my_string[i] in vowels:
            continue
        else:
            res += my_string[i]
            
    return res

# def solution(my_string):
#     vowels = ['a','e','i','o','u']
#     for vowel in vowels:
#         my_string = my_string.replace(vowel, '')
#     return my_string