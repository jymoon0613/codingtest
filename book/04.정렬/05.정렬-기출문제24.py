# 안테나

## 나의 답안 ##

N = int(input())

houses = list(map(int, input().split()))

houses.sort()

all_dist = []
for i in houses:
    dist = []
    for j in houses:
        dist.append(abs(i-j))
    all_dist.append(sum(dist))
    
m = 1e+9
res = 0
for i in range(len(all_dist)):
    print(m)
    if all_dist[i] < m:
        m = all_dist[i]
        res = i

print(houses[res])

## 예시 답안 ##

n = int(input())

data = list(map(int, input().split()))

data.sort()

print(data[(n-1) // 2])