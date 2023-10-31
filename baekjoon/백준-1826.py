# 1826: 연료 채우기

import sys
import heapq

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(array, (a,b))

l, p = map(int, input().split())

q = []
result = 0
while p < l:
    while array and p >= array[0][0]:
        a, b = heapq.heappop(array)
        heapq.heappush(q, (-b, a))

    if not q:
        result = -1
        break

    b, a = heapq.heappop(q)
    p -= b
    result += 1

print(result)