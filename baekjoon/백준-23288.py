# 23288: 주사위 굴리기 2

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

# 위, 북, 동, 서, 남, 뒤
dice = [1, 2, 3, 4, 5, 6]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def roll_dice(dice, d):
    # 동
    if d == 0:
        new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    # 북
    elif d == 1:
        new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    # 서
    elif d == 2:
        new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    # 남
    else:
        new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    return new_dice

def bfs(x, y, num):

    visited = [[False] * m for _ in range(n)]

    total = 1

    q = deque()

    q.append((x,y))

    visited[x][y] = True

    while q:
        
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if array[nx][ny] == num and visited[nx][ny] == False:
                    total+= 1
                    visited[nx][ny] = True
                    q.append((nx,ny))

    return total * num

result = 0
d = 0
x, y = 0, 0
nx, ny = x, y
cnt = 0

score = [[-1] * m for _ in range(n)]

while cnt < k:

    nx += dx[d]
    ny += dy[d]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[d]
        ny -= dy[d]
        d = (d+2) % 4
        continue

    dice = roll_dice(dice, d)

    if score[nx][ny] == -1:
        score[nx][ny] = bfs(nx, ny, array[nx][ny])

    result += score[nx][ny]

    if dice[-1] == array[nx][ny]:
        d = d
    elif dice[-1] > array[nx][ny]:
        d = (d-1) % 4
    else:
        d = (d+1) % 4

    x, y = nx, ny

    cnt += 1

print(result)