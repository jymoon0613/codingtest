# 17144: 미세먼지 안녕!

import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())

array = []
machine = [] # 위, 아래
dusts = []
for i in range(r):
    array.append(list(map(int, input().split())))
    for j in range(c):
        if array[i][j] == -1:
            machine.append((i,j))
        elif array[i][j] != 0:
            dusts.append((i,j,array[i][j]))
        else:
            continue

# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def get_score(array):

    total = 0
    for i in range(r):
        for j in range(c):
            if array[i][j] != -1:
                total += array[i][j]
    return total

def move_dust():

    delta = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if array[x][y] not in [0,-1]:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= 0 and nx < r and ny >= 0 and ny < c and array[nx][ny] != -1:
                        delta[nx][ny] += int(array[x][y] / 5)
                        cnt += 1
                array[x][y] -= (int(array[x][y] / 5) * cnt)

    for x in range(r):
        for y in range(c):
            array[x][y] += delta[x][y]

def clean_up():

    dxdy = [[0,1], [-1,0], [0,-1], [1,0]]

    d = 0

    mx, my = machine[0]

    x, y = mx, my+1

    prev = 0

    while True:

        nx = x + dxdy[d][0]
        ny = y + dxdy[d][1]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue

        array[x][y], prev = prev, array[x][y]

        x, y = nx, ny

        if x == mx and y == my:
            break

def clean_down():

    dxdy = [[0,1], [1,0], [0,-1], [-1,0]]

    d = 0

    mx, my = machine[1]

    x, y = mx, my+1

    prev = 0

    while True:

        nx = x + dxdy[d][0]
        ny = y + dxdy[d][1]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue

        array[x][y], prev = prev, array[x][y]

        x, y = nx, ny

        if x == mx and y == my:
            break

cnt = 0
while cnt < t:

    move_dust()

    clean_up()

    clean_down()

    cnt += 1

print(get_score(array))