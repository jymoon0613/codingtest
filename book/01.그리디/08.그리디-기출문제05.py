# 볼링공 고르기

## 나의 답안 ##

n, m = map(int, input().split())

k = list(map(int, input().split()))

table = [0] * (m+1)

for i in k:
    table[i] += 1

total = sum(table)
result = 0
for i in table:
    result += i * (total - i)
    total -= i

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