# 연구소

## 나의 답안 ##

from itertools import combinations

N, M = map(int, input().split())

graph = []
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    
virus = []
possible = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i, j))
            graph[i][j] = 0
        elif graph[i][j] == 0:
            possible.append((i, j))
        else:
            continue
            
candidates = list(combinations(possible, 3))

def dfs(x, y, g):
    
    if x >= N or x < 0 or y >= M or y < 0:
        return False
    
    if g[x][y] == 0:
        
        g[x][y] = 2

        dfs(x+1, y, g)
        dfs(x-1, y, g)
        dfs(x, y+1, g)
        dfs(x, y-1, g)
    
    return True

res = []
for c in candidates:
    c1, c2, c3 = c
    graph[c1[0]][c1[1]] = 1
    graph[c2[0]][c2[1]] = 1
    graph[c3[0]][c3[1]] = 1
    
    for (x, y) in virus:
        dfs(x, y, graph)
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
                
    res.append(cnt)
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                graph[i][j] = 0
                
    graph[c1[0]][c1[1]] = 0
    graph[c2[0]][c2[1]] = 0
    graph[c3[0]][c3[1]] = 0

print(max(res))

## 예시 답안 ##

n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
                
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
                
    return score

def dfs(count):
    global result
    
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
                
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
                    
        result = max(result, get_score())
        
        return
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
                
dfs(0)
print(result)