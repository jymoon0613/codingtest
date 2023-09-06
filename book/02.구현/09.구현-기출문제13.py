# 치킨 배달

## 나의 답안 ##

from itertools import combinations

n, m = map(int, input().split())

array = []

chickens = []
houses = []
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(n):
        if array[i][j] == 2:
            chickens.append((i,j))
        if array[i][j] == 1:
            houses.append((i,j))

candidates = combinations(chickens, m)

result = int(1e+9)
for candidate in candidates:

    sum_value = 0
    for house in houses:

        min_dist = int(1e+9)
        for chicken in candidate:

            dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

            min_dist = min(min_dist, dist)

        sum_value += min_dist

    result = min(result, sum_value)

print(result)

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