# 경쟁적 전염

## 나의 답안 ##

from collections import deque

N, K = map(int, input().split())

viruses = [[] for _ in range(K)]
graph = []
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            viruses[graph[i][j]-1].append((i, j))
    
S, X, Y = map(int, input().split())

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def search():
    queues = []
    for i in range(K):
        queues.append(deque(viruses[i]))
    
    second = 0
    while True:
        
        second += 1
        
        for i in range(K):
            queue = queues[i]
            
            if len(queue) == 0:
                continue
            
            x, y = queue.popleft()
            
            for dx, dy in zip(dxs, dys):
                
                xx = x + dx
                yy = y + dy
            
                if xx < 0 or xx >= N or yy < 0 or yy >= N:
                    continue
                    
                if graph[xx][yy] != 0:
                    continue
                    
                graph[xx][yy] = i + 1
                
                queue.append((xx, yy))
        
        cnt = 0
        for i in range(K):
            
            cnt += len(queues[i])
            
        if cnt == 0:
            break
        
        if second == S:
            print(graph[X-1][Y-1])
            break
            
search()

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