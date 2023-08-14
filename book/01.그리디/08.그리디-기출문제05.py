# 볼링공 고르기

## 나의 답안 ##

n, m = map(int, input().split())
k = list(map(int, input().split()))

array = [0] * n

for i in k:
    array[i-1] += 1

result = 0
for i in range(m):
    n -= array[i]
    result += array[i] * n

print(result)

## 예시 답안 ##

n, m = map(int, input().split())
data= list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)