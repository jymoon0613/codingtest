# 만들 수 없는 금액

## 나의 답안 ##

n = int(input())
data = list(map(int, input().split()))

data.sort()
result = 1

for d in data:
    if d > result:
        break
    else:
        result += d

print(result)

## 예시 답안 ##

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

for x in data:
    if x > target:
        break
    else:
        target += x

print(target)