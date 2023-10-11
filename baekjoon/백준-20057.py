# 20057: 마법사 상어와 토네이도

import sys

input = sys.stdin.readline

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

filter = [
    [0,    0,   0.02, 0,    0],
    [0,    0.1, 0.07, 0.01, 0],
    [0.05, 0,   0,    0,    0],
    [0,    0.1, 0.07, 0.01, 0],
    [0,    0,   0.02, 0,    0]]

def rotate_matrix_by_90(array):

    n = len(array)
    m = len(array[0])

    temp = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            temp[n-j-1][i] = array[i][j]

    return temp

filters = [filter]
for _ in range(3):
    filter = rotate_matrix_by_90(filter)
    filters.append(filter)

alphas = [(2, 1), (3, 2), (2, 3), (1, 2)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y = n // 2, n // 2
result = 0
cnt = 0
turn = 2
d = 0
filter = filters[d]
while not (x == 0 and y == 0):

    x += dx[d]
    y += dy[d]
    cnt += 1
    target = array[x][y]
    array[x][y] = 0
    remain = target
    for i in range(5):
        for j in range(5):
            value = int(target * filter[i][j])
            remain -= value
            if (x+i-2) < 0 or (x+i-2) >= n or (y+j-2) < 0 or (y+j-2) >= n:
                result += value
            else:
                array[x+i-2][y+j-2] += value
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        result += remain
    else:
        array[nx][ny] += remain

    if cnt == (turn // 2) or cnt == turn:
        d = (d+1) % 4
        filter = filters[d]
        if cnt == turn:
            cnt = 0
            turn += 2

print(result)