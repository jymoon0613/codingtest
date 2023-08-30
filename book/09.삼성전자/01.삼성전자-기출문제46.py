# 아기 상어 

## 나의 답안 ##

from collections import deque

n = int(input())

all_fishes = []
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(n):
        if array[i][j] == 9:
            sx, sy, ss = i, j, 2
        elif array[i][j] != 0:
            all_fishes.append((array[i][j], i, j))
        else:
            continue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(array, shark, fish, ss):
    
    time_table = [[0] * n for _ in range(n)]

    sx, sy = shark

    fx, fy = fish

    q = deque()

    q.append((sx, sy))

    while q:

        x, y = q.popleft()

        if x == fx and y == fy:

            return time_table[x][y]
        
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if array[nx][ny] > ss:
                continue

            if time_table[nx][ny] == 0: 

                time_table[nx][ny] = time_table[x][y] + 1
                q.append((nx, ny))

    return -1

def get_fishes(all_fishes, shark):

    fishes = [fish for fish in all_fishes if fish[0] < shark[0]]

    if len(fishes) >= 2:
        fishes.sort(key=lambda x: abs(x[1]-shark[1]) + abs(x[2]-shark[2]))

    return fishes

result = 0
ate = 0
while True:

    fishes = get_fishes(all_fishes, (ss, sx, sy))

    if len(fishes) == 0:
        break

    fs, fx, fy = fishes[0]

    time = bfs(array, (sx, sy), (fx, fy), ss)

    result += time

    array[fx][fy] = 0
    array[sx][sy] = 0

    sx, sy = fx, fy

    all_fishes.remove((fs, fx, fy))

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
