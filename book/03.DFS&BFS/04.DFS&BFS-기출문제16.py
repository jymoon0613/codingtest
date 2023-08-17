# 연구소

## 나의 답안 ##

import copy
from itertools import combinations

n, m = map(int, input().split())

array = []
possibles = []
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(m):
        if array[i][j] == 0:
            possibles.append((i, j))

def calculate(array):
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                result += 1

    return result

def dfs(array, x, y):

    if x < 0 or x >= n or y < 0 or y >= m:

        return False
    
    if array[x][y] == 0:
        
        array[x][y] = 2

        dfs(array, x-1, y)
        dfs(array, x+1, y)
        dfs(array, x, y-1)
        dfs(array, x, y+1)

    return True

candidates = combinations(possibles, 3)
result = -1
for candidate in candidates:
    array_copy = copy.deepcopy(array)
    for x, y in candidate:
        array_copy[x][y] = 1
    for i in range(n):
        for j in range(m):
            if array_copy[i][j] == 2:
                array_copy[i][j] = 0
                dfs(array_copy, i, j)

    result = max(result, calculate(array_copy))

print(result)

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