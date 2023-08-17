# 특정 거리의 도시 찾기

## 나의 답안 ##

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [0] * (n+1)

def bfs(graph, start, distance):

    q = deque()

    q.append(start)

    distance[start] = 1

    while q:
        
        x = q.popleft()

        for i in graph[x]:
            if distance[i] == 0:
                distance[i] = distance[x] + 1
                q.append(i)

    result = []
    for i in range(n+1):
        if distance[i] == (k+1):
            result.append(i)

    if len(result) == 0:
        print(-1)
    else:
        for r in result:
            print(r)

bfs(graph, x, distance)

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

