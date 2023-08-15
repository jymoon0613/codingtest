# 문자열 압축

## 나의 답안 ##

s = input()

result = []
for i in range(1, len(s)+1):
    d = dict()
    for j in range(0, len(s)-i, i):
        left = s[j:j+i]
        right = s[j+i:j+2*i]

        if left == right:
            if right in d.keys():
                d[right] += 1
            else:
                d[right] = 2

    length = len(s) - (i * (sum(d.values()) - len(d)))  + len(d)
    
    result.append(length)

print(min(result))

## 예시 답안 ##

s = input()

answer = len(s)

for step in range(1, len(s) // 2 + 1):
    
    compressed = ''
    
    prev = s[0:step]
    count = 1
    
    for j in range(step, len(s), step):
        
        if prev == s[j:j+step]:
            count += 1
        
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = s[j:j+step]
            count = 1
            
    compressed += str(count) + prev if count >= 2 else prev
    
    answer = min(answer, len(compressed))
    
print(answer)