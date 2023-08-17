# 음료수 얼려 먹기

## 나의 답안 ##

n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(array, x, y):

    array[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:

            if array[nx][ny] == 0:
                dfs(array, nx, ny)

result = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            dfs(array, i, j)
            result += 1

print(result)

## 예시 답안 ##

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y>= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        
        return True
    
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            
print(result)