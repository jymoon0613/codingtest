# 15683: 감시

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = []
cctvs = []
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(m):
        if array[i][j] >= 1 and array[i][j] < 6:
            cctvs.append((array[i][j], i, j))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

modes = [
    [],
    [[0], [1], [2], [3]],
    [[0,1], [2,3]],
    [[0,2], [0,3], [1,2], [1,3]],
    [[0,1,2], [0,1,3], [0,2,3], [1,2,3]],
    [[0,1,2,3]]
]

def get_score(array):
    value = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                value += 1

    return value

def get_copy(array):

    temp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            temp[i][j] = array[i][j]

    return temp

def dfs(array, mode, x, y):

    for d in mode:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or array[nx][ny] == 6:
                break
            if array[nx][ny] == 0:
                array[nx][ny] = 7

    return array
    
result = int(1e+9)
def search(array, cnt):

    global result

    if cnt == len(cctvs):
        result = min(result, get_score(array))
        return
    
    else:

        temp = get_copy(array)

        cctv = cctvs[cnt]
        for mode in modes[cctv[0]]:
            temp = dfs(temp, mode, cctv[1], cctv[2])
            search(temp, cnt+1)
            temp = get_copy(array)

search(array, 0)
print(result)