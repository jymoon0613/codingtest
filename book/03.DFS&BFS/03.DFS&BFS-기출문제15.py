# 특정 거리의 도시 찾기

## 나의 답안 ##

from collections import deque

def bfs(matrix, X, visited, N, K):
    
    queue = deque()
    
    queue.append(X)
    
    visited[X] = 1
    
    dist = [0 for _ in range(N)]
    
    while queue:
        x = queue.popleft()
        for i in matrix[x]:
            if visited[i] == 0:
                queue.append(i)
                if visited[i] == 1:
                    continue
                else:
                    dist[i] = dist[x] + 1
                    
                visited[i] = 1
    
    cnt = 0
    for i in range(N):
        if dist[i] == K:
            cnt += 1
            print(i+1)
    if cnt == 0:
        print(-1)

N, M, K, X = map(int, input().split())

matrix = [[] for _ in range(N)]

for _ in range(M):
    start, end = map(int, input().split())
    matrix[start-1].append(end-1)
    
visited = [0 for _ in range(N)]
        
print(bfs(matrix, X-1, visited, N, K))

## 예시 답안 ##

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    
    for next_node in graph[now]:
        
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)

