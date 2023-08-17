# 미로 탈출

## 나의 답안 ##

from collections import deque

n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(array, start):

    q = deque()

    q.append(start)

    array[start[0]][start[1]] = 1

    while q:

        x, y = q.popleft()

        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if array[nx][ny] == 1:
                q.append((nx, ny))
                array[nx][ny] = array[x][y] + 1

    print(array[n-1][m-1])

bfs(array, (0,0))

## 예시 답안 ##

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    
    queue.append((x, y))
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if graph[ny][ny] == 0:
                continue
                
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]
            
print(bfs(0, 0))