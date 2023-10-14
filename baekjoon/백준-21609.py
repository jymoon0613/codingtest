# 21609: 상어 중학교

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

def rotate_matrix_by_90(array):

    temp = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            temp[n-y-1][x] = array[x][y]

    return temp

def gravity():

    for r in range(n-2, -1, -1):
        for c in range(n):
            if array[r][c] >= 0:
                nr = r
                while True:
                    if (nr+1) < n and array[nr+1][c] == -2:
                        array[nr+1][c] = array[nr][c]
                        array[nr][c] = -2
                        nr += 1
                    else:
                        break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, num):

    q = deque()
    q.append((x,y))
    visited[x][y] = 0

    num_bk, num_rb = 0, 0
    blocks_, rainbows_ = [(x,y)], []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny]:
                if array[nx][ny] == num:
                    blocks_.append((nx, ny))
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    num_bk += 1
                elif array[nx][ny] == 0:
                    rainbows_.append((nx,ny))
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    num_bk += 1
                    num_rb += 1

    for x,y in rainbows_:
        visited[x][y] = 0

    blocks_.sort()

    base = blocks_[0]

    return num_bk, num_rb, base, blocks_ + rainbows_

def get_score():
    num_bk = 0
    num_rb = 0
    block_index = []
    normal_blocks = []
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 1:
                num_bk += 1
                if array[x][y] == 0:
                    num_rb += 1
                else:
                    normal_blocks.append((x,y))
                block_index.append((x,y))
    
    normal_blocks.sort()
    base_block = normal_blocks[0]

    return num_bk, num_rb, base_block, block_index

result = 0

while True:

    visited = [[0] * n for _ in range(n)]
    blocks = []

    for x in range(n):
        for y in range(n):
            if array[x][y] >= 1 and not visited[x][y]:
                num_bk, num_rb, base, block_inds = bfs(x, y, array[x][y])
                if num_bk >= 2:
                    blocks.append((num_bk, num_rb, base[0], base[1], block_inds))

    blocks.sort(reverse=True)
    if len(blocks) == 0:
        break
    
    group = blocks[0]

    result += (group[0] ** 2)
    for (x,y) in group[-1]:
        array[x][y] = -2

    gravity()

    array = rotate_matrix_by_90(array)

    gravity()

print(result)