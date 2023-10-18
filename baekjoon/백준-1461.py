# 1461: 도서관

from collections import deque

n, m = map(int, input().split())

pos = list(map(int, input().split()))

left = [abs(p) for p in pos if p < 0]
right = [p for p in pos if p > 0]

left.sort(reverse=True)
right.sort(reverse=True)

m_ = 0
dist = []
for i in range(len(left) // m):
    dist.append(left[i*m])

if len(left) % m > 0:
    dist.append(left[(len(left) // m)*m])

for i in range(len(right) // m):
    dist.append(right[i*m])

if len(right) % m > 0:
    dist.append(right[(len(right) // m)*m])

dist.sort()
result = dist.pop()
result += 2 * sum(dist)
print(result)