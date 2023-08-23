# 효율적인 화폐 구성

## 나의 답안 ##

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

INF = int(1e+9)
d = [INF] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != INF:
            d[j] = min(d[j], d[j-array[i]] + 1)
    
if d[m] == INF:
    print(-1)
else:
    print(d[m])

## 예시 답안 ##

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
    
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)
    
res = d[m]

if d[m] == 10001:
    print(-1)
else:
    print(d[m])