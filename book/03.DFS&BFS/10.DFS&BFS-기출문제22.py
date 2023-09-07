# 블록 이동하기

## 나의 답안 ##

import json
from collections import deque

board = input()
board = json.loads(board)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def all_moves(board, robot):

    result = []
    
    lx, ly, rx, ry = robot

    for i in range(4):

        nlx = lx + dx[i]
        nly = ly + dy[i]
        nrx = rx + dx[i]
        nry = ry + dy[i]

        if board[nlx][nly] != 1 and board[nrx][nry] != 1:
            result.append((nlx, nly, nrx, nry))

    if lx == rx:
        if board[lx-1][ly] != 1 and board[rx-1][ry] != 1:
            result.append((lx, ly, lx-1, ly))
            result.append((rx, ry, rx-1, ry))
        if board[lx+1][ly] != 1 and board[rx+1][ry] != 1:
            result.append((rx+1, ry, rx, ry))
            result.append((lx+1, ly, lx, ly))

    if ly == ry:
        if board[lx][ly-1] != 1 and board[rx][ry-1] != 1:
            result.append((rx, ry-1, rx, ry))
            result.append((lx, ly-1, lx, ly))
        if board[lx][ly+1] != 1 and board[rx][ry+1] != 1:
            result.append((rx, ry, rx, ry+1))
            result.append((lx, ly, lx, ly+1))

    return result

def solution(board):

    board_new = [[1] * (len(board)+2) for _ in range(len(board)+2)]

    for i in range(len(board)):
        for j in range(len(board)):
            board_new[i+1][j+1] = board[i][j]

    cost = 0

    robot = (cost, (1, 1, 1, 2))

    q = deque()
    q.append(robot)

    while q:

        visited = []

        cost, robot = q.popleft()

        if (robot[0], robot[1]) == (len(board_new)-2, len(board_new)-2) or (robot[2], robot[3]) == (len(board_new)-2, len(board_new)-2):
            
            return cost

        moves = all_moves(board_new, robot)

        for move in moves:

            if move not in visited:

                q.append((cost + 1, move))
            
    return 0
            
print(solution(board))

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