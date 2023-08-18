# 감시 피하기

## 나의 답안 ##

n = int(input())

graph = []
num_T = 0
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            num_T += 1

graph_copy = [[0] * n for _ in range(n)]

def check(graph, x, y, d):

    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    
    if graph[x][y] == 'O':
        return True

    if graph[x][y] == 'S':
        return False
    
    if d == 0:
        if not check(graph, x+1, y, 0):
            return False

    if d == 1:
        if not check(graph, x-1, y, 1):
            return False
        
    if d == 2:
        if not check(graph, x, y-1, 2):
            return False
        
    if d == 3:
        if not check(graph, x, y+1, 3):
            return False

    return True


def solution(cnt):

    if cnt == 3:
        for i in range(n):
            for j in range(n):
                graph_copy[i][j] = graph[i][j]

        res = 0
        for i in range(n):
                for j in range(n):
                    if graph_copy[i][j] == 'T':
                        for k in range(4):
                            if not check(graph_copy, i, j, k):
                                return False
                            
                        res += 1

                        if res == num_T:
                            return True

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                cnt += 1
                graph[i][j] = 'O'
                if solution(cnt):
                    return True
                cnt -= 1
                graph[i][j] = 'X'
    
    return False

result = solution(0)
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