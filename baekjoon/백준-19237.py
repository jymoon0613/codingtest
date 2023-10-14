# 19237: 어른 상어

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

MAP = [[[-1, 0] for _ in range(n)] for _ in range(n)]

priorities = [[] for _ in range(m)]

fishes = [[] for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] != 0:
            MAP[i][j][0] = data[j]-1
            MAP[i][j][1] = k
            fishes[data[j]-1].append((i,j))

directions = list(map(int, input().split()))

for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

def move_fishes():

    for num in range(m):
        if fishes[num][0] == (-1,-1):
            continue
        
        x, y = fishes[num].pop()
        d = directions[num]

        possible = False
        for i in range(4):
            nd = priorities[num][d-1][i]
            nx = x + dx[nd-1]
            ny = y + dy[nd-1]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and MAP[nx][ny][1] == 0:
                possible = True
                fishes[num].append((nx, ny))
                directions[num] = nd
                break

        if not possible:
            for i in range(4):
                nd = priorities[num][d-1][i]
                nx = x + dx[nd-1]
                ny = y + dy[nd-1]
                if nx >= 0 and nx < n and ny >= 0 and ny < n and MAP[nx][ny][0] == num:
                    fishes[num].append((nx, ny))
                    directions[num] = nd
                    break

    for i in range(m):
        for j in range(i+1,m):
            if fishes[i][0] != (-1,-1) or fishes[j][0] != (-1,-1):
                if fishes[i][0] == fishes[j][0]:
                    fishes[j].pop()
                    fishes[j].append((-1,-1))

    for num in range(m):
        if fishes[num][0] != (-1,-1):
            MAP[fishes[num][0][0]][fishes[num][0][1]][0] = num
            MAP[fishes[num][0][0]][fishes[num][0][1]][1] = k

def move_map():
    for x in range(n):
        for y in range(n):
            if MAP[x][y][0] != -1:
                if MAP[x][y][1] == k:
                    if fishes[MAP[x][y][0]][0] != (x,y):
                        MAP[x][y][1] -= 1
                else:
                    MAP[x][y][1] -= 1

                if MAP[x][y][1] == 0:
                    MAP[x][y][0] = -1

result = 0

while True:

    value = 0
    for i in range(m):
        if fishes[i][0] != (-1,-1):
            value += 1

    if value < 2:
        break

    if result >= 1000:
        result = -1
        break

    move_fishes()

    move_map()

    result += 1

print(result)