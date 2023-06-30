# 게임 개발

N, M = list(map(int, input().split()))

A, B, d = list(map(int, input().split()))

array = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visits = []

visits.append((A, B))

cnt = 0
while True:
    
    d += 1
    
    if d > 3:
        d = 0
        
    cnt = 0
    for ddx, ddy in zip(dx, dy):
        A_next = A + ddx
        B_next = B + ddy
        
        if array[B_next][A_next] == 1:
            cnt += 1
            
        if (A_next, B_next) in visits:
            cnt += 1
            
    if cnt == 4:
        A_next = A - dx[d]
        B_next = B - dy[d]
        
        if array[B_next][A_next] == 1:
            break
            
        visits.append((A_next, B_next))
        A = A_next
        B = B_next
        
    else:
        A_next = A + dx[d]
        B_next = B + dy[d]
        
        if (A_next, B_next) in visits:
            continue
            
        visits.append((A_next, B_next))
        A = A_next
        B = B_next
    
print(len(visits))

## 답안 예시

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())

d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
count = 1
turn_time = 0

while True:
    
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
        
    else:
        turn_time += 1
        
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if array[nx][ny] == 0:
            x = nx
            y = ny
            
        else:
            break
            
        turn_time = 0
        
print(count)