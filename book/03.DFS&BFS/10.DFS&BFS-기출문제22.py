# 블록 이동하기

## 나의 답안 ##

import json
from collections import deque

board = input()
board = json.loads(board)
        
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0
visited =[]
def solution(board):

    lx, ly, rx, ry, cnt = 0, 0, 0, 1, 0

    q = deque()

    q.append((lx, ly, rx, ry, cnt))

    visited.append((lx, ly, rx, ry))

    goal = (len(board)-1, len(board)-1)
    while q:

        lx, ly, rx, ry, cnt = q.popleft()

        if (lx, ly) == goal or (rx, ry) == goal:
            print(cnt)
            break

        for i in range(4):
            
            nlx = lx + dx[i]
            nly = ly + dy[i]
            nrx = rx + dx[i]
            nry = ry + dy[i]

            if nlx < 0 or nrx < 0 or nlx >= len(board) or nrx >= len(board) or nly < 0 or nry < 0 or nly >= len(board) or nry >= len(board):

                continue

            if board[nlx][nly] == 1 or board[nrx][nry] == 1:

                continue
            
            if (nlx, nly, nrx, nry) not in visited:
                q.append((nlx, nly, nrx, nry, cnt+1))
                visited.append((nlx, nly, nrx, nry))

        if lx == rx:
            for i in [-1, 1]:
                nlx = lx + i
                nrx = rx + i

                if nlx < 0 or nlx >= len(board) or nrx < 0 or nrx >= len(board):
                    
                    continue

                if board[nlx][ly] == 1 or board[nrx][ry] == 1:

                    continue
                
                if (lx, ly, nlx, ly, cnt+1) not in visited:
                    q.append((lx, ly, nlx, ly, cnt+1))
                    visited.append((lx, ly, nlx, ly))
                if (lx, ly, nlx, ly, cnt+1) not in visited:
                    q.append((rx, ry, nrx, ry, cnt+1))
                    visited.append((rx, ry, nrx, ry))

        if ly == ry:
            for i in [-1, 1]:
                nly = ly + i
                nry = ry + i

                if nly < 0 or nly >= len(board) or nry < 0 or nry >= len(board):
                    
                    continue

                if board[lx][nly] == 1 or board[rx][nry] == 1:

                    continue
                
                if (lx, ly, nlx, ly, cnt+1) not in visited:
                    q.append((lx, ly, lx, nly, cnt+1))
                    visited.append((lx, ly, lx, nly))
                if (rx, ry, rx, nry, cnt+1) not in visited:
                    q.append((rx, ry, rx, nry, cnt+1))
                    visited.append((rx, nry, rx, ry))

solution(board)

## 예시 답안 ##

import json
from collections import deque

board = input()
board = json.loads(board)

def get_next_pos(pos, board):
    
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
            
        if pos1_x == pos2_x:
            for i in [-1, 1]: 
                if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                    next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                    next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
                    
        elif pos1_y == pos2_y:
            for i in [-1, 1]:
                if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                    next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                    next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
                
    return next_pos
    
def solution(board):
    
    n = len(board)
    
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
            
    q = deque()
    visited = []
    pos = {(1,1), (1,2)}
    q.append((pos, 0))
    visited.append(pos)
    
    while q:
        pos, cost = q.popleft()
        
        if (n,n) in pos:
            return cost
        
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
                
    return 0

print(solution(board))