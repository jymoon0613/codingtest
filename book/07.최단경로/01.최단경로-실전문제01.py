# 미래 도시

## 나의 답안 ##

n, m = map(int, input().split())

INF = int(1e+9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

target1, target2 = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

dist1 = graph[1][target2]
dist2 = graph[target2][target1]

if dist1 == INF or dist2 == INF:
    print(-1)
else:
    print(dist1 + dist2)

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