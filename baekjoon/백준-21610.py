# 21610: 마법사 상어와 비바라기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

ds = [list(map(int, input().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for d, s in ds:

    moved = []
    for x, y in cloud:
        nx = (x + (s * dx[d-1])) % n
        ny = (y + (s * dy[d-1])) % n

        array[nx][ny] += 1

        moved.append((nx, ny))

    for x, y in moved:
        for k in range(1, 8, 2):

            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and array[nx][ny] != 0:
                array[x][y] += 1

    cloud_new = []
    for i in range(n):
        for j in range(n):
            if (i,j) not in moved and array[i][j] >= 2:
                array[i][j] -= 2
                cloud_new.append((i,j))

    cloud = cloud_new

result = 0
for i in range(n):
    for j in range(n):
        result += array[i][j]

print(result)