# 11000: 강의실 배정

import heapq
import sys

input = sys.stdin.readline

n = int(input())

lecture = []
for _ in range(n):
    s, t = map(int, input().split())
    lecture.append((s,t))

lecture.sort()

classroom = []
heapq.heappush(classroom, lecture[0][1])

for i in range(1, n):
    if classroom[0] > lecture[i][0]:
        heapq.heappush(classroom, lecture[i][1])
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, lecture[i][1])

print(len(classroom))