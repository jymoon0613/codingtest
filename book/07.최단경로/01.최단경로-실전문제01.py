# 미래 도시

## 나의 답안 ##

import heapq

INF = int(1e+9)
n, m = map(int, input().split())

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

def search(start):
    
    q = []
    heapq.heappush(q, (0, start))
    
    distance[start] = 0
        
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
search(1)

tok = distance[k]

distance = [INF] * (n+1)

search(k)

tox = distance[x]

res = tok + tox

if tox == INF:
    print(-1)
else:
    print(res)

## 예시 답안 ##

INF = int(1e+9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
         for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
    
else:
    print(distance)