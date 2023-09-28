# 3190: 뱀

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board = [[0] * n for _ in range(n)]

for _ in range(int(input())):
    x, y = map(int, input().split())

    board[x-1][y-1] = 1

directions = []
for _ in range(int(input())):
    t, d = input().split()
    directions.append((int(t), d))

x, y, d = 0, 0, 0
snake = deque()
snake.append((x, y))
board[x][y] = 2

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

result = 0
ind = 0
while True:

    result += 1

    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
        break

    if board[nx][ny] != 1:
        px, py = snake.popleft()
        board[px][py] = 0

    x, y = nx, ny
    board[x][y] = 2
    snake.append((x, y))

    if result == (directions[ind][0]):

        if directions[ind][1] == 'L':
            d = (d + 1) % 4

        else:
            d = (d + 3) % 4

        if ind < (len(directions)-1):
            ind += 1

print(result)

