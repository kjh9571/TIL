n = int(input())
cnt = 0

while n != 0:
    word = input()
    set_word = set(word)
    
    for i in range(len(word)):
        if word[i] not in set_word:
            break
        
        if word[i] != word[i-1] and i != 0:
            set_word.remove(word[i-1])
            # print(word[i])
            # print(set_word)
            
        if i == len(word)-1:
            cnt += 1
            
    n -= 1

print(cnt)