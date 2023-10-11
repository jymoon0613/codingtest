# 17142: 연구소 3

import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

array = []
cnt_0_ = 0
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(n):
        if array[i][j] == 0:
            array[i][j] = '/'
            cnt_0_ += 1
        elif array[i][j] == 1:
            array[i][j] = '-'
        else:
            array[i][j] = '*'

temp = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_value = int(1e+9)
def search(sx, sy, cnt):

    global min_value, cnt_0

    local_max = 0

    if cnt == m:
        cnt_0 = cnt_0_
        viruses = []
        for x in range(n):
            for y in range(n):
                temp[x][y] = array[x][y]
                if temp[x][y] == 0:
                    heapq.heappush(viruses, (0, x, y))

        while viruses:
            
            time, x, y = heapq.heappop(viruses)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n and temp[nx][ny] != '-':
                    if temp[nx][ny] == '/':
                        temp[nx][ny] = time + 1
                        local_max = max(local_max, time+1)
                        heapq.heappush(viruses, (time+1, nx, ny))
                        cnt_0 -= 1
                    elif temp[nx][ny] == '*':
                        temp[nx][ny] = time + 1
                        heapq.heappush(viruses, (time+1, nx, ny))                     

        if cnt_0 == 0:
            min_value = min(local_max, min_value)
        return

    else:
        for x in range(sx, n):
            if x == sx:
                y_ = sy
            else:
                y_ = 0
            for y in range(y_, n):
                if array[x][y] == '*':
                    array[x][y] = 0
                    search(x, y, cnt+1)
                    array[x][y] = '*'

        return
    
search(0,0,0)

if min_value == int(1e+9):
    print(-1)
else:
    print(min_value)