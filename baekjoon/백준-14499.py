# 14499: 주사위 굴리기

import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

moves = list(map(int, input().split()))

# 위, 북, 동, 서, 남, 아래
dice = [0] * 6

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move_dice(dice, direction):

    if direction == 1:
        dice_new = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        return dice_new
    
    elif direction == 2:
        dice_new = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        return dice_new
    
    elif direction == 3:
        dice_new = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        return dice_new
    else:
        dice_new = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
        return dice_new
    
for move in moves:

    nx = x + dx[move-1]
    ny = y + dy[move-1]

    if nx >= 0 and nx < n and ny >= 0 and ny < m:
        x, y = nx, ny
        dice = move_dice(dice, move)
        print(dice[0])
        if array[x][y] == 0:
            array[x][y] = dice[-1]
        else:
            dice[-1] = array[x][y]
            array[x][y] = 0        