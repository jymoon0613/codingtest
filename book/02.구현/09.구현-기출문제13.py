# 치킨 배달

## 나의 답안 ##

import itertools

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        point = city[i][j]
        if point == 1:
            houses.append((i,j))
        elif point == 2:
            chickens.append((i,j))
        else:
            continue

chickens_combs = list(itertools.combinations(chickens, M))

res = []
for chickens_comb in chickens_combs:
    chicken_dist = []
    for house in houses:
        minimum = 999
        for chicken in chickens_comb:
            dist = abs(chicken[0]-house[0]) + abs(chicken[1]-house[1])
            if dist < minimum:
                minimum = dist
        chicken_dist.append(minimum)
        
    res.append(sum(chicken_dist))

print(min(res))

## 예시 답안 ##

from itertools import combinations

n, m = map(int, input().split())

chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))
            
candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
            
        result += temp
        
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
    
print(result)