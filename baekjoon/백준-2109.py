# 2109: 순회강연

import heapq

n = int(input())
array = []
for _ in range(n):
    p, d = map(int, input().split())
    array.append((p,d))

array.sort(key=lambda x: (x[1]))

q = []
for i in range(n):
    heapq.heappush(q, array[i][0])
    if len(q) > array[i][1]:
        heapq.heappop(q)

print(sum(q))