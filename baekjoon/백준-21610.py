# 21610: 마법사 상어와 비바라기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

ds = [list(map(int, input().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for d, s in ds:

    cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

    for i in range(4):
        cloud[i][0] += s * dx[d-1]
        cloud[i][1] += s * dy[d-1]

    print(cloud)

    for i in range(4):
        cloud[i][0] %= n
        cloud[i][1] %= n

    print(cloud)

    for c in cloud:
        x, y = c
        array[x][y] += 1

    for c in cloud:
        value = 0
        x, y = c
        for k in range(1, 8, 2):

            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if array[nx][ny] != 0:
                    value += 1
        array[x][y] += value

    for i in range(n):
        for j in range(n):
            print(array[i][j], end=' ')
        print()
    print()

    for i in range(n):
        for j in range(n):
            if [i,j] not in cloud:
                if array[i][j] >= 2:
                    array[i][j] -= 2

    for i in range(n):
        for j in range(n):
            print(array[i][j], end=' ')
        print()
    print()

result = 0
for i in range(n):
    for j in range(n):
        result += array[i][j]

print(result)



    