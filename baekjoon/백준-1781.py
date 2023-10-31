# 1781: 컵라면

import heapq
import sys

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(array, (a, b))

q = []
for i in range(n):
    x = heapq.heappop(array)
    heapq.heappush(q, x[1])
    if len(q) > x[0]:
        heapq.heappop(q)

print(sum(q))