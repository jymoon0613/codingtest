# 14503: 로봇 청소기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

x, y, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board[x][y] = -1
result = 1

while True:

    possible = False
    for _ in range(4):

        d = (d + 3) % 4

        nx = x + dx[d]
        ny = y + dy[d]

        if board[nx][ny] == 0:
            x = nx
            y = ny
            board[x][y] = -1
            result += 1
            possible = True
            break

    if not possible:
        nx = x - dx[d]
        ny = y - dy[d]

        if board[nx][ny] == 1:
            break

        else:
            x = nx
            y = ny

print(result)