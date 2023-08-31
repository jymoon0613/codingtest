# 만들 수 없는 금액

## 나의 답안 ##

n = int(input())

array = list(map(int, input().split()))

array.sort()

target = 1
for i in range(n):
    if target < array[i]:
        break
    else:
        target += array[i]

print(target)

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