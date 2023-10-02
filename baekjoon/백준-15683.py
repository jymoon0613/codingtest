# 15683: 감시

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

temp = [[0] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def get_score(array):
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                result += 1

    return result

def dfs(x, y, d):

    nx = x + dx[d]
    ny = y + dy[d]

    if nx >= 0 and nx < n and ny >= 0 and ny < m and temp[nx][ny] != 6:
        temp[nx][ny] = 1
        dfs(nx, ny, d)
    
def search(r, c, num):

    pass

global_min = int(1e+9)
for i in range(n):
    for j in range(m):
        if array[i][j] >= 1 and array[i][j] < 6:
            global_min = min(global_min, search(i, j, array[i][j]))

print(global_min)