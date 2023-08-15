# 문자열 재정렬

## 나의 답안 ##

s = input()

nums = []
alps = []
for i in range(len(s)):
    if s[i].isnumeric():
        nums.append(int(s[i]))
    else:
        alps.append(s[i])

nums.sort()
alps.sort(key=lambda x: ord(x))

alps = ''.join(alps)

print(alps + str(sum(nums)))

## 예시 답안 ##

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
        
    else:
        value += int(x)
        
result.sort()

if value != 0:
    result.append(str(value))
    
print(''.join(result))
