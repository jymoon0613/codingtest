# 뱀

## 나의 답안 ##

from collections import deque

n = int(input())
k = int(input())

array = [[0] * (n) for _ in range(n)]

array[0][0] = 2

for _ in range(k):
    a, b = map(int, input().split())
    array[a-1][b-1] = 1

l = int(input())

directions = []
for _ in range(l):
    
    x, c = input().split()

    directions.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, d = 0, 0, 0
array[x][y] = 2
q = deque()
q.append((x, y))

time = directions[0][0]
ind = 0

result = 0
while True:

    result += 1

    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or array[nx][ny] == 2:
        break

    if array[nx][ny] == 1:
        array[nx][ny] = 2

    else:
        array[nx][ny] = 2

        px, py = q.popleft()
        array[px][py] = 0

    x = nx
    y = ny
    q.append((nx, ny))

    if result == time:

        if directions[ind][1] == 'D':
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4

        ind += 1

        if ind < l:
            time = directions[ind][0]

print(result)

## 답안 예시 ##

n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4

    else:
        direction = (direction + 1) % 4

    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0

            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))

        else:
            time += 1
            break
        
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time

print(simulate())