# 숨바꼭질

## 나의 답안 ##

import heapq

INF = int(1e+9)

n, m = map(int, input().split())

distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))
    
start = 1
q = [(0, start)]
distance[start] = 0

while q:
    
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[0]
        
        if cost < distance[i[1]]:
            distance[i[1]] = cost
            heapq.heappush(q, (cost, i[1]))
            
max_value = -1
ind = None
for i in range(1, n+1):
    if distance[i] > max_value:
        max_value = distance[i]
        ind = i
        
print(ind, max_value, distance.count(max_value))

## 예시 답안 ##

import heapq
import sys

input = sys.stdin.readline
INF = int(1e+9)

n, m = map(int, input().split())

start = 1

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)    

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

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
            
max_node = 0
max_distance = 0
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
        
print(max_node, max_distance, len(result))