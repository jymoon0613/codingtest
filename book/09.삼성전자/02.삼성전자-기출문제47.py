# 청소년 상어

## 나의 답안 ##

import copy

array = [[] for _ in range(4)]

all_fishes = []

for i in range(4):
    data = list(map(int, input().split()))
    for step in range(0, 8, 2):
        a, b = data[step:step+2]
        array[i].append([a, b-1])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(array, num):

    for i in range(4):
        for j in range(4):
            if array[i][j][0] == num:
                return (i, j)
            
    return None

def move_fishes(array, sx, sy):

    for fish_num in range(1, 17):
        
        position = find_fish(array, fish_num)

        if position != None:

            fx, fy = position
        
            fd = array[fx][fy][1]

            for i in range(8):

                nx = fx + dx[fd]
                ny = fy + dy[fd]

                if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
                    if (nx, ny) != (sx, sy):
                        array[fx][fy][1] = fd
                        array[fx][fy], array[nx][ny] = array[nx][ny], array[fx][fy]
                        break

                fd = (fd + 1) % 8

def get_possible_positions(array, x, y):
    positions = []
    direction = array[x][y][1]
    
    for i in range(4):
        x += dx[direction]
        y += dy[direction]
        
        if 0 <= x and x < 4 and 0 <= y and y < 4:
            if array[x][y][0] != -1:
                positions.append((x, y))
                
    return positions

result = 0
def dfs(array, x, y, total):

    global result

    array = copy.deepcopy(array)

    total += array[x][y][0]
    array[x][y][0] = -1

    move_fishes(array, x, y)

    positions = get_possible_positions(array, x, y)

    if len(positions) == 0:
        result = max(result, total)
        return
    
    for nx, ny in positions:
        dfs(array, nx, ny, total)

dfs(array, 0, 0, 0)
print(result)

## 예시 답안 ##

import copy

array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    
    for j in range(4):
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]
        
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(direction):
    
    return (direction + 1) % 8

result = 0

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
            
    return None

def move_all_fishes(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                        
                direction = turn_left(direction)
                
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
                
    return positions

def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)
    
    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1
    
    move_all_fishes(array, now_x, now_y)
    
    positions = get_possible_positions(array, now_x, now_y)
    
    if len(positions) == 0:
        result = max(result, total)
        return
    
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)
        
dfs(array, 0, 0, 0)
print(result)