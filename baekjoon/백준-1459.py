# 1459: 걷기

from collections import deque
import copy

tx, ty, w, s = map(int, input().split())

MAP = [[0] * max(w,s) for _ in range(max(w,s))]

delta = [
    [[-1, 1, 0, 0], [0, 0, -1, 1]],
    [[-1, 1, 1, -1], [1, -1, 1, -1]]
]

cost = [w, s]

sx, sy = 0, 0

def search(array,sx,sy,mode):

    q = deque()
    q.append((sx,sy))

    while q:

        x, y = q.popleft()

        if (x,y) == (tx,ty):
            return array[x][y]

        for i in range(4):
            nx = x + delta[mode][0][i]
            ny = y + delta[mode][1][i]

            if nx >= 0 and nx < max(w,s) and ny >= 0 and ny < max(w,s):
                if array[nx][ny] == 0 and (nx,ny) != (sx,sy):
                    array[nx][ny] = array[nx][ny] + cost[mode]
                    q.append((nx,ny))


print(search(copy.deepcopy(MAP), 0, 0, 0))
print(search(copy.deepcopy(MAP), 0, 0, 1))