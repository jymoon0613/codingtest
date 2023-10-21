# 1374: 강의실

import heapq

n = int(input())

arr = []
for _ in range(n):
    a, b, c = map(int, input().split())
    arr.append((b,c))

arr.sort()

classroom = []
_, c = arr[0]
heapq.heappush(classroom, c)

for i in range(1, n):
    if arr[i][0] >= classroom[0]:
        heapq.heappop(classroom)
        heapq.heappush(classroom, arr[i][1])
    else:
        heapq.heappush(classroom, arr[i][1])

print(len(classroom))