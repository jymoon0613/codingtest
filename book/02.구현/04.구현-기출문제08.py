# 문자열 재정렬

## 나의 답안 ##

S = list(input())

alps = []
nums = []

for s in S:
    if s.isnumeric() == True:
        nums.append(int(s))
    
    else:
        alps.append(s)
        
nums = sum(nums)
alps.sort(key=lambda x: ord(x))

alps.append(str(nums))

res = ''.join(alps)

print(res)

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
