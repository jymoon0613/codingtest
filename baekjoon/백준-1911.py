# 1911: 흙길 보수하기

import heapq

n, l = map(int, input().split())

array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a,b))

array.sort()

cur = array[0][0]

result = 0
for i in range(n):
    a, b = array[i]
    if a > cur:
        cur = a
    dist = b - cur
    cnt = dist // l
    if dist % l != 0:
        cnt += 1
    cur = cur + cnt * l
    result += cnt 

print(result)