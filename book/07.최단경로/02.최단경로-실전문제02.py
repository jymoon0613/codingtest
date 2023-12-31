# 전보

## 나의 답안 ##

import heapq

INF = int(1e+9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

q = []

heapq.heappush(q, (0, c))

distance[c] = 0

for x in graph[c]:
    distance[x[0]] = x[1]

while q:

    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for x in graph[now]:
        cost = dist + x[1]

        if cost < distance[x[0]]:
            distance[x[0]] = cost
            heapq.heappush(q, (cost, x[0]))

cnt = 0
max_distance = -1
for i in range(1, n+1):
    if distance[i] != INF:
        max_distance = max(max_distance, distance[i])
        cnt += 1

print(cnt-1, max_distance)

## 예시 답안 ##

import heapq
import sys

input = sys.stdin.readline
INF = int(1e+9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)


for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
def dijkstra(start):
    
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
                
dijkstra(start)

cnt = 0
max_distance = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt-1, max_distance)