# 16235: 나무 재테크

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

array = [[5] * n for _ in range(n)]

trees = [[deque() for _ in range(n)] for _ in range(n)]

a = [list(map(int, input().split())) for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring_summer():
    for x in range(n):
        for y in range(n):
            l = len(trees[x][y])
            for i in range(l):
                if trees[x][y][i] > array[x][y]:
                    for _ in range(i,l):
                        array[x][y] += trees[x][y].pop() // 2
                    break
                else:
                    array[x][y] -= trees[x][y][i]
                    trees[x][y][i] += 1

def fall_winter():
    for x in range(n):
        for y in range(n):
            l = len(trees[x][y])
            for i in range(l):
                if trees[x][y][i] % 5 == 0:
                    for j in range(8):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if nx >= 0 and nx < n and ny >= 0 and ny < n:
                            trees[nx][ny].appendleft(1)
            array[x][y] += a[x][y]

cnt = 0

for _ in range(k):
    spring_summer()
    fall_winter()

    cnt += 1

result = 0
for x in range(n):
    for y in range(n):
        result += len(trees[x][y])

print(result)