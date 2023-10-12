# 20058: 마법사 상어와 파이어스톰

import sys
from collections import deque

input = sys.stdin.readline

n, q = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(2**n)]
total = 0
for x in range(len(array)):
    total += sum(array[x])

stages = list(map(int, input().split()))

nn = 2**n

out = deque()
for l in stages:
    ll = 2**l
    temp = [[0] * (nn) for _ in range(nn)]
    offset_x = 0
    for x in range(0, nn, ll):
        offset_y = 0
        for y in range(0, nn, ll):
            for xx in range(ll):
                for yy in range(ll):
                    temp[yy+offset_x][ll-xx-1+offset_y] = array[xx+offset_x][yy+offset_y]
            offset_y += ll
        offset_x += ll

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(nn):
        for y in range(nn):
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < nn and ny >= 0 and ny < nn and temp[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:
                out.append((x,y))
    
    while out:
        x, y = out.popleft()
        if temp[x][y] > 0:
            temp[x][y] -= 1
            total -= 1

    array = temp

max_value = 0
def bfs(x,y):

    global max_value

    local_cnt = 1

    q = deque()

    q.append((x,y))

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < nn and ny >= 0 and ny < nn and temp[nx][ny] > 0:
                if temp[nx][ny] != -1:
                    temp[nx][ny] = -1
                    local_cnt += 1
                    q.append((nx,ny))

    max_value = max(max_value, local_cnt)

for x in range(nn):
    for y in range(nn):
        if temp[x][y] > 0:
            temp[x][y] = -1
            bfs(x,y)

print(total, max_value)