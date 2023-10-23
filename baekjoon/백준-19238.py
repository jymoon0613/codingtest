# 19238: 스타트 택시

import heapq

n, m, k = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

MAX = int(1e+9)

tx, ty = map(int, input().split())

tx -= 1
ty -= 1

cnt = 2
passenger = []
for _ in range(m):
    x, y, a, b = map(int, input().split())
    passenger.append((x-1,y-1,a-1,b-1))
    MAP[x-1][y-1] = cnt
    cnt += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_psg(sx, sy):

    visited = [[False] * n for _ in range(n)]

    q = []
    heapq.heappush(q, (0, sx, sy))
    visited[sx][sy] = True

    passenger_ = []

    while q:

        cost, x, y = heapq.heappop(q)

        if MAP[x][y] > 1:
            passenger_.append((cost,x,y,MAP[x][y]))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if MAP[nx][ny] != 1 and not visited[nx][ny]: 
                    visited[nx][ny] = True
                    q.append((cost+1,nx,ny))

    if len(passenger_) == 0:
        return MAX
    else:
        passenger_.sort()
        return passenger_[0]
    
def bfs_dst(sx, sy, px, py):

    visited = [[False] * n for _ in range(n)]

    q = []
    heapq.heappush(q, (0, sx, sy))
    visited[sx][sy] = True

    while q:

        cost, x, y = heapq.heappop(q)

        if (x,y) == (px,py):
            return cost

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if MAP[nx][ny] != 1 and not visited[nx][ny]: 
                    visited[nx][ny] = True
                    q.append((cost+1, nx,ny))

    return MAX

CNT = 0
possible = True
while True:

    if CNT == m:
        print(k)
        break

    psg = bfs_psg(tx, ty)

    if psg == MAX:
        print(-1)
        break
                
    k -= psg[0]

    if k < 0:
        print(-1)
        break

    px, py, pdx, pdy = passenger[psg[-1]-2]
    
    dist = bfs_dst(px, py, pdx, pdy)

    if dist == MAX:
        print(-1)
        break

    k -= dist

    if k < 0:
        print(-1)
        break

    k += (dist * 2)
    tx, ty = pdx, pdy

    MAP[px][py] = 0
    CNT += 1