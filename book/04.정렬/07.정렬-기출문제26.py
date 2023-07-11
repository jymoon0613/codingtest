# 카드 정렬하기

## 나의 답안 ##

N = int(input())

data = []
for _ in range(N):
    data.append(int(input()))
    
data.sort()
res = 0

while True:

    new_data = []
    for i in range(0, len(data), 2):
        part = data[i:i+2]
        
        if len(part) == 2:
            res += sum(part)
        
        new_data.append(sum(part))
        
    if len(new_data) == 1:
        break
        
    else:
        data = new_data

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