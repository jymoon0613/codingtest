# 곱하기 혹은 더하기

## 나의 답안 ##

s = input()

result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])

    if result <= 1 or num <= 1:
        result += num
    else :
        result *= num

print(result)

## 예시 답안 ##

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else :
        result *= num

print(result)