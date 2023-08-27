# 화성 탐사

## 나의 답안 ##

import heapq

INF = int(1e+9)

for t in range(int(input())):
    n = int(input())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    q = []

    heapq.heappush(q, (graph[0][0], 0, 0))

    distance = [[INF] * n for _ in range(n)]

    distance[0][0] = graph[0][0]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0
    while q:

        c, x, y = heapq.heappop(q)

        if distance[x][y] < c:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                
                cost = c + graph[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])

## 예시 답안 ##

import heapq
import sys

input = sys.stdin.readline

INF = int(1e+9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(int(input())):

    n = int(input())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
        
    distance = [[INF] * n for _ in range(n)]
    
    x, y = 0, 0
    
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]
    
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
                
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])