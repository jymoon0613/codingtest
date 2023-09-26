# 아기 상어 

## 나의 답안 ##

from collections import deque

n = int(input())
INF = int(1e+9)

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(n):
        if array[i][j] == 9:
            sx, sy, ss = i, j, 2

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    
    time = [[-1] * n for _ in range(n)]

    q = deque()

    q.append((sx, sy))

    array[sx][sy] = 0
    time[sx][sy] = 0

    while q:

        x, y = q.popleft()
        
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or array[nx][ny] > ss:
                continue

            if time[nx][ny] == -1: 

                time[nx][ny] = time[x][y] + 1
                q.append((nx, ny))

    return time

def find_fish(time):

    min_dist = INF
    for i in range(n):
        for j in range(n):
            if time[i][j] != -1 and array[i][j] >= 1 and array[i][j] < ss:
                if time[i][j] < min_dist:
                    min_dist = time[i][j]
                    fx, fy = i, j

    if min_dist == INF:
        return None
    else:
        return (fx, fy, min_dist)

result = 0
ate = 0
while True:

    fish = find_fish(bfs())

    if fish == None:
        break

    result += fish[2]

    sx, sy = fish[0], fish[1]

    array[fish[0]][fish[1]] = 0

    ate += 1

    if ate == ss:
        ate = 0
        ss += 1

print(result)

## 예시 답안 ##

from collections import deque

INF = int(1e+9)

n = int(input())

array = []
for i in range(n):
    
    array.append(list(map(int, input().split())))
    
now_size = 2
now_x, now_y = 0, 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0
            
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    dist = [[-1] * n for _ in range(n)]
    
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
                    
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist
    
result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        
        array[now_x][now_y] = 0
        ate += 1
        
        if ate >= now_size:
            now_size += 1
            ate = 0
