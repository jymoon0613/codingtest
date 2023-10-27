# 12018: Yonsei TOTO

import heapq

n, m = map(int, input().split())

subject = []
for i in range(n):
    a, b = map(int, input().split())
    point = list(map(int, input().split()))
    if a < b:
        heapq.heappush(subject, 1)
    else:
        point.sort(reverse=True)
        heapq.heappush(subject, point[b-1])

result = 0
for i in range(n):
    p = heapq.heappop(subject)
    if (m - p) >= 0:
        m -= p
        result += 1
    else:
        break

print(result)