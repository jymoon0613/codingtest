# 1202: 보석도둑

import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

array = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(array, (m,v))

c = [int(input()) for _ in range(k)]

c.sort()

q = []
result = 0
for i in range(k):
    while array and c[i] >= array[0][0]:
        heapq.heappush(q, -heapq.heappop(array)[1])
    if q:
        result -= heapq.heappop(q)
    
print(result)