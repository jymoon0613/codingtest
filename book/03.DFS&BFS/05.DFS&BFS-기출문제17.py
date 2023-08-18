# 경쟁적 전염

## 나의 답안 ##

from collections import deque

n, k = map(int, input().split())

graph = []
q = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            q.append((graph[i][j], 0, i, j))

q.sort(key=lambda x: x[0])
q = deque(q)

s, x, y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while q:

    virus, t, xx, yy = q.popleft()

    if t == s:
        break

    for i in range(4):

        nx = xx + dx[i]
        ny = yy + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] != 0:
            continue
        
        graph[nx][ny] = virus
        q.append((virus, t+1, nx, ny))
        
print(graph[x-1][y-1])

## 예시 답안 ##

from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    
    graph.append(list(map(int, input().split())))
    
    for j in range(n):
        
        if graph[i][j] != 0:
            
            data.append((graph[i][j], 0, i, j))
            
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()
    
    if s == target_s:
        break
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx and nx < n and 0<= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))
                
print(graph[target_x-1][target_y-1])