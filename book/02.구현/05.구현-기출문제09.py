# 문자열 압축

## 나의 답안 ##

s = list(input())

all_tokens = []
for l in range(1, len(s)):
    tokens = []
    s_prev = None
    for i in range(0, len(s), l):
        s_pres = ''.join(s[i:i+l])
        s_next = ''.join(s[i+l:i+2*l])

        if s_pres == s_next:
            if s_next == s_prev:
                tokens = [(i[0], i[1]+1) if i[0] == s_pres else i for i in tokens]

            else:
                tokens.append((s_pres, 2))

        else:
            if s_prev == s_pres:
                pass
            else:
                tokens.append((s_pres, 1))

        s_prev = s_pres

    all_tokens.append(tokens)
            
            
all_tokens.append([(''.join(s), 1)])

res = [''.join([''.join([str(i[1]), i[0]]) if i[1] != 1 else ''.join([i[0]]) for i in ts]) for ts in all_tokens]

res = [len(i) for i in res]

print(min(res))

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