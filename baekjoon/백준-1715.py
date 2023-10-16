# 1715: 카드 정렬하기 

import heapq

n = int(input())

q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

result = 0
while len(q) > 1:

    num1 = heapq.heappop(q)
    num2 = heapq.heappop(q)

    result += (num1 + num2)

    heapq.heappush(q, num1 + num2)

print(result)