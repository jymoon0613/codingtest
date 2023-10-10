# 16235: 나무 재테크

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

array = [[5] * n for _ in range(n)]

a = [list(map(int, input().split())) for _ in range(n)]

trees = deque()
for _ in range(m):
    trees.append(map(int, input().split()))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring_summer():
    for i in range(len(trees)):
        x, y, age = trees.popleft()
        if age > array[x-1][y-1]:
            temp[x-1][y-1] += (age // 2)
            continue
        else:
            array[x-1][y-1] -= age
            age += 1
            trees.append((x, y, age))

def fall_winter():
    cnt = 0
    for i in range(len(trees)):
        x, y, age = trees[i+cnt]
        if age % 5 == 0:
            for j in range(8):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx >= 1 and nx < (n+1) and ny >= 1 and ny < (n+1):
                    trees.appendleft((nx, ny, 1))
                    cnt += 1

def winter():
    for x in range(n):
        for y in range(n):
            array[x][y] += temp[x][y]

cnt = 0
while cnt < k:

    spring_and_summer()
    fall()
    winter()

    cnt += 1

print(len(trees))