def solution(my_string):
    
    nums = set([f'{i}' for i in range(0, 10)])
    result = []
    
    for i in my_string:
        if i in nums:
            result.append(int(i))
            
    return sorted(result)

# def solution(my_string):
#     return sorted([int(c) for c in my_string if c.isdigit()]