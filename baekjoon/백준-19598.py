# 19598: 최소 회의실 개수

import heapq

n = int(input())

q = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(q, (a,b))

a, b = heapq.heappop(q)
end = []
heapq.heappush(end, b)

for i in range(1, n):
    a, b = heapq.heappop(q)
    e = heapq.heappop(end)
    if a >= e:
        heapq.heappush(end, b)
    else:
        heapq.heappush(end, b)
        heapq.heappush(end, e)

print(len(end))