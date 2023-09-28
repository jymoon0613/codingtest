# 16234: 인구 이동

import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, index):

    global count, total

    q = deque()

    q.append((x,y))

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and union[nx][ny] == -1:
                diff = abs(array[nx][ny] - array[x][y])
                if diff >= l and diff <= r:
                    union[nx][ny] = index
                    total += array[nx][ny]
                    count += 1
                    q.append((nx, ny))

result = 0
while True:

    union = [[-1] * n for _ in range(n)]
    update = []

    index = 0
    count = 0
    total = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                union[i][j] = index
                total += array[i][j]
                count += 1
                bfs(i, j, index)
                update.append(int(total/count))
                total = 0
                count = 0
                index += 1

    if len(update) == (n*n):
        break

    result += 1

    for i in range(n):
        for j in range(n):
            array[i][j] = update[union[i][j]]

print(result)