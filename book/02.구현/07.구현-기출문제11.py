# 뱀

## 나의 답안 ##

def move(board, snake, direction):
    
    n = len(board)
    apple = False
    
    if direction == 'R':
        r_next = snake[-1][0]
        c_next = snake[-1][1] + 1
        
        if c_next >= n:
            return 0
        
        elif board[r_next][c_next] == 2:
            return 0
        
        else:
            if board[r_next][c_next] == 1:
                apple = True
            board[r_next][c_next] = 2
            snake.append((r_next, c_next))
            
    elif direction == 'L':
        r_next = snake[-1][0]
        c_next = snake[-1][1] - 1
        
        if c_next < 0:
            return 0
        
        elif board[r_next][c_next] == 2:
            return 0
        
        else:
            if board[r_next][c_next] == 1:
                apple = True
            board[r_next][c_next] = 2
            snake.append((r_next, c_next))
            
    elif direction == 'U':
        r_next = snake[-1][0] - 1
        c_next = snake[-1][1]
        
        if r_next < 0:
            return 0
        
        elif board[r_next][c_next] == 2:
            return 0
        
        else:
            if board[r_next][c_next] == 1:
                apple = True
            board[r_next][c_next] = 2
            snake.append((r_next, c_next))
            
    else:
        r_next = snake[-1][0] + 1
        c_next = snake[-1][1]
        
        if r_next >= n:
            return 0
        
        elif board[r_next][c_next] == 2:
            return 0
        
        else:
            if board[r_next][c_next] == 1:
                apple = True
            board[r_next][c_next] = 2
            snake.append((r_next, c_next))
            
    if apple == False:
        r_tail, c_tail = snake.pop(0)
        board[r_tail][c_tail] = 0
        
    return board, snake, direction
        
N = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

# 뱀 초기위치 지정
board[0][0] = 2

K = int(input())

for i in range(K):
    r, c = map(int, input().split())
    
    board[r-1][c-1] = 1
    
L = int(input())

# snake
snake = []
# row, col, length
current = (0, 0)
snake.append(current)
# direction
direction_now = 'R'

moves = []
total_time = 0
for l in range(L):
    
    second, direction_next = list(input().split())
    
    moves.append((int(second), direction_next))

cnt = 0

second, direction_next = moves.pop(0)

while True:
    
    cnt += 1
    result = move(board, snake, direction=direction_now)
    
    if (result == 0):
        break
        
    else:
        board, snake, direction_now = result
                
    if cnt == second:
        
        if (direction_now == 'D') and (direction_next == 'D'):
        
            direction_now = 'L'
            
        elif (direction_now == 'D') and (direction_next == 'L'):
            
            direction_now = 'R'
        
        elif (direction_now == 'U') and (direction_next == 'D'):
            
            direction_now = 'R'
            
        elif (direction_now == 'U') and (direction_next == 'L'):
            
            direction_now = 'L'
            
        elif (direction_now == 'R') and (direction_next == 'D'):
            
            direction_now = 'D'
            
        elif (direction_now == 'R') and (direction_next == 'L'):
            
            direction_now = 'U'
            
        elif (direction_now == 'L') and (direction_next == 'D'):
            
            direction_now = 'U'
            
        else:
            
            direction_now = 'D'
        
        if len(moves) != 0:
            second, direction_next = moves.pop(0)
        
print(cnt)

## 답안 예시 ##

n = int(input())
k = int(input())

data = [[0] * (n+1) for _ in range(n+1)]

info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4

    else:
        direction = (direction + 1) % 4

    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0

            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))

        else:
            time += 1
            break
        
        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time

print(simulate())