# 감시 피하기

## 나의 답안 ##

import copy

n = int(input())

graph = []
for _ in range(n):
    graph.append(input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check(graph, x, y):

    for i in range(4):

        nx, ny = x, y

        while True:

            nx = nx + dx[i]
            ny = ny + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:

                break

            if graph[nx][ny] == 'O':

                break

            if graph[nx][ny] == 'S':

                return False
            
    return True

def dfs(graph, cnt):

    if cnt == 3:
        graph_copy = copy.deepcopy(graph)
        for i in range(n):
            for j in range(n):
                if graph_copy[i][j] == 'T':
                    if not check(graph_copy, i, j):
                        return False
                    
        return True

    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    cnt += 1
                    if dfs(graph, cnt):
                        return True
                    graph[i][j] = 'X'
                    cnt -= 1

        return False

result = dfs(graph, 0)

if result:
    print('YES')
else:
    print('NO')

## 예시 답안 ##

from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
            
        if board[i][j] == 'X':
            spaces.append((i, j))
            
def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            
            y -= 1
            
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            
            y += 1
            
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            
            x -= 1
            
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            
            x += 1
            
    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
        
    return False

find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
        
    if not process():
        find = True
        break
        
    for x, y in data:
        board[x][y] = 'X'
        
if find:
    print('YES')
    
else:
    print('NO')