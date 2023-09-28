# 15686: 치킨 배달

from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

houses = []
chickens = []

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(n):
        if array[i][j] == 1:
            houses.append((i, j))
        elif array[i][j] == 2:
            chickens.append((i, j))
        else:
            continue

candidates = combinations(chickens, m)

result = int(1e+9)
for candidate in candidates:
    distance = 0
    for house in houses:
        min_value = int(1e+9)
        for chicken in candidate:
            min_value = min(min_value, (abs(chicken[0]-house[0]) + abs(chicken[1]-house[1])))
        distance += min_value
    result = min(result, distance)

print(result)