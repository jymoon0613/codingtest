# 카드 정렬하기

## 나의 답안 ##

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort()
accumulated = 0
def solution(array):

    global accumulated

    if len(array) <= 2:
        if len(array) == 2:
            accumulated += sum(array)
            return sum(array)
        else:
            return sum(array)

    point = (len(array) - 1) // 2

    return solution(array[:point+1]) + solution(array[point+1:])

last = solution(array)

result = last + accumulated

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