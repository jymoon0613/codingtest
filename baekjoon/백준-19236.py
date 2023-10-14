# 19236: 청소년 상어

import sys
import copy

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

MAP = [[[] for _ in range(4)] for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    ind = 0
    for j in range(0, 8, 2):
        a, b = data[j], data[j+1]
        MAP[i][ind].append((a,b-1))
        ind += 1

result = 0

def get_fish_position(MAP, index):

    for x in range(4):
        for y in range(4):
            if MAP[x][y][0][0] == index:
                return (x, y)
            
    return None


def move_fish(MAP, shark):

    for index in range(1, 17):
        position = get_fish_position(MAP, index)

        if position == None:
            continue

        x, y = position
        d = MAP[x][y][0][1]

        nd = (d-1) % 8

        for i in range(8):

            nd = (nd + 1) % 8

            nx = x + dx[nd]
            ny = y + dy[nd]

            if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
                if (nx, ny) != (shark[0], shark[1]):
                    MAP[nx][ny], MAP[x][y] = MAP[x][y], MAP[nx][ny]
                    num, _ = MAP[nx][ny].pop()
                    MAP[nx][ny].append((num, nd))
                    break
        
    return MAP

def search(MAP, shark, value):

    global result

    x, y, d = shark

    if x < 0 or x >= 4 or y < 0 or y >= 4:
        result = max(result, value)
        return

    if MAP[x][y][0][0] == -1:
        return
    
    num, d = MAP[x][y].pop()

    MAP[x][y].append((-1,-1))

    MAP = move_fish(MAP, shark)

    nx = x
    ny = y
    for _ in range(4):

        nx += dx[d]
        ny += dy[d]

        MAP_ = copy.deepcopy(MAP)
        search(MAP_, (nx, ny, d), value + num)

search(MAP, (0, 0, 0), 0)

print(result)