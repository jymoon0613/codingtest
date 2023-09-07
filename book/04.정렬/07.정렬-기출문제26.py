# 카드 정렬하기

## 나의 답안 ##

import heapq

n = int(input())

q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

result = 0
while q:

    if len(q) <= 1:
        break

    x1 = heapq.heappop(q)
    x2 = heapq.heappop(q)

    result += x1
    result += x2

    heapq.heappush(q, x1+x2)

print(result)

## 예시 답안 ##

import heapq

n = int(input())

heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
    
result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
    
print(result)