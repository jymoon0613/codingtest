# 인구 이동

## 나의 답안 ##

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    
    global graph, union, total_number, sumed_value
    
    sumed_value += graph[x][y]
    total_number += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            diff = abs(graph[x][y] - graph[nx][ny])
            if diff >= l and diff <= r:
                if union[nx][ny] == 0:
                    union[nx][ny] = union[x][y]
                    dfs(nx, ny)

result = 0
while True:
    
    union = [[0] * n for _ in range(n)]
    values = []
    
    union_num = 1
    total_number = 0
    sumed_value = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == 0:
                union[i][j] = union_num
                dfs(i, j)
                values.append(sumed_value // total_number)
                union_num += 1
                total_number = 0
                sumed_value = 0
                                
    for i in range(n):
        for j in range(n):
            graph[i][j] = values[union[i][j]-1]
        
    if len(values) == (n**2):
        break
    else:
        result += 1
        
print(result)

## 예시 답안 ##

from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index):
    
    united = []
    united.append((x, y))
    
    q = deque()
    q.append((x, y))
    
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
                    
    for i, j in united:
        graph[i][j] = summary // count
        
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    
    total_count += 1
    
print(total_count)