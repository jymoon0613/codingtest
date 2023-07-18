# 효율적인 화폐 구성

## 나의 답안 ##

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
    
d = [1e-9] * 10001
d[0] = 0

for i in range(1, m+1):
    for j in array:
        if i % j == 0:
            d[i] = min(d[i-j]+1, d[i])
            
        if d[i] == 1e-9:
            d[i] = 10001
        
res = d[m]

if d[m] != 10001:
    print(d[m])
else:
    print(-1)

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