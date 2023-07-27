# 화성 탐사

## 나의 답안 ##

import heapq

INF = int(1e+9)

def search(start):

    q = []

    heapq.heappush(q, (graph[start[0]][start[1]], start))

    distance[start[0]][start[1]] = graph[start[0]][start[1]]

    while q:

        dist, now = heapq.heappop(q)

        if distance[now[0]][now[1]] < dist:
            continue

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx < n and nx >= 0 and ny < n and ny >= 0:
                cost = dist + graph[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(int(input())):

    n = int(input())

    distance = [[INF] * n for _ in range(n)]

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    search((0, 0))

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