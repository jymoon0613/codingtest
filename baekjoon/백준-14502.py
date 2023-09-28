# 14502: 연구소

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(board, x, y):

    board[x][y] = 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if board[nx][ny] == 0:
                virus(board, nx, ny)

def check(board):

    result = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                result += 1

    return result

max_value = 0
def dfs(board, cnt):

    global max_value

    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(temp, i, j)

        max_value = max(max_value, check(temp))

    else:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    board[i][j] = 1
                    cnt += 1
                    dfs(board, cnt)
                    board[i][j] = 0
                    cnt -= 1

dfs(board, 0)

print(max_value)