# 3109: 빵집

import copy

r, c = map(int, input().split())

array = []
for _ in range(r):
    array.append(list(input()))

dx = [-1, 0, 1]
dy = [1, 1, 1]

def dfs(x,y):
    if y == (c-1):
        return True
    else:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                if array[nx][ny] != 'x':
                    array[nx][ny] = 'x'
                    if dfs(nx,ny):
                        return True
                    
    return False

result = 0
for i in range(r):
    if dfs(i,0):
        result += 1

print(result)