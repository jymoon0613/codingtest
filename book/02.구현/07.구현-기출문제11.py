# 뱀

## 나의 답안 ##

n = int(input())

array = [[0] * n for _ in range(n)]

k = int(input())

for _ in range(k):
    x, y = map(int, input().split())
    array[x-1][y-1] = 1

l = int(input())

directions = []
for _ in range(l):
    t, d = input().split()
    directions.append((int(t), d))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

xs, ys, ds = 0, 0, 0

snakes = []
array[xs][ys] = 2
snakes.append((xs, ys))

end = False
result = 0
ind = 0
t, d_next = directions[0]
while True:

    result += 1

    nx = xs + dx[ds]
    ny = ys + dy[ds]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or array[nx][ny] == 2:
        end = True
        break
    else:
        if array[nx][ny] == 1:
            array[nx][ny] = 2
        else:
            array[nx][ny] = 2
            x, y = snakes.pop(0)
            array[x][y] = 0

    xs, ys = nx, ny
    snakes.append((xs, ys))

    if ind < l and result == directions[ind][0]:

        if directions[ind][1] == 'D':
            ds = (ds + 1) % 4
        else:
            ds = (ds + 3) % 4

        ind += 1

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