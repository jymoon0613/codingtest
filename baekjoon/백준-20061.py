# 20061: 모노미노도미노 2

import sys

input = sys.stdin.readline

n = int(input())

blocks = []
for _ in range(n):
    t, x, y = map(int, input().split())
    blocks.append((t,x,y))

BLUE = [[0] * 6 for _ in range(4)]
GREEN = [[0] * 4 for _ in range(6)]

def block_blue(t, x, y):
    if t == 1:
        col_ind = 0
        for c in range(6):
            if BLUE[x][c] == 1:
                break
            else:
                col_ind = c
        BLUE[x][col_ind] = 1

    elif t == 2:
        col_ind = 0
        for c in range(6):
            if BLUE[x][c] == 1:
                break
            else:
                col_ind = c
        BLUE[x][col_ind] = 1
        BLUE[x][col_ind-1] = 1

    else:
        col_ind = 0
        for c in range(6):
            if BLUE[x][c] == 1 or BLUE[x+1][c] == 1:
                break
            else:
                col_ind = c
        BLUE[x][col_ind] = 1
        BLUE[x+1][col_ind] = 1

def block_green(t, x, y):
    if t == 1: 
        row_ind = 0
        for r in range(6):
            if GREEN[r][y] == 1:
                break
            else:
                row_ind = r
        GREEN[row_ind][y] = 1
    elif t == 2:
        row_ind = 0
        for r in range(6):
            if GREEN[r][y] == 1 or GREEN[r][y+1] == 1:
                break
            else:
                row_ind = r
        GREEN[row_ind][y] = 1
        GREEN[row_ind][y+1] = 1
    else:
        row_ind = 0
        for r in range(6):
            if GREEN[r][y] == 1:
                break
            else:
                row_ind = r
        GREEN[row_ind][y] = 1
        GREEN[row_ind-1][y] = 1

score = 0

def score_blue():

    global score

    ind = 5
    while ind > -1:

        value = 0
        for r in range(4):
            value += BLUE[r][ind]

        if value == 4:
            score += 1
            for r in range(4):
                for c in range(ind, -1, -1):
                    if c == ind:
                        BLUE[r][c] = 0
                    else:
                        BLUE[r][c+1], BLUE[r][c] = BLUE[r][c], BLUE[r][c+1]
        
        else:
            ind -= 1
            continue
    
    cnt = 0
    for c in range(2):
        for r in range(4):
            if BLUE[r][c] == 1:
                cnt += 1
                break
    
    while cnt > 0:
        
        for r in range(4):
            for c in range(5, -1, -1):
                if c == 5:
                    BLUE[r][c] = 0
                else:
                    BLUE[r][c+1], BLUE[r][c] = BLUE[r][c], BLUE[r][c+1]
        
        cnt -= 1

def score_green():

    global score

    ind = 5
    while ind > -1:

        value = sum(GREEN[ind])

        if value == 4:
            score += 1
            for r in range(ind, -1, -1):
                for c in range(4):
                    if r == ind:
                        GREEN[r][c] = 0
                    else:
                        GREEN[r+1][c], GREEN[r][c] = GREEN[r][c], GREEN[r+1][c]
        else:
            ind -= 1
            continue

    cnt = 0
    for r in range(2):
        if sum(GREEN[r]) > 0:
            cnt += 1

    while cnt > 0:

        for r in range(5,-1,-1):
            for c in range(4):
                if r == 5:
                    GREEN[r][c] = 0
                else:
                    GREEN[r+1][c], GREEN[r][c] = GREEN[r][c], GREEN[r+1][c]

        cnt -=1
    
for block in blocks:

    t, x, y = block

    block_blue(t,x,y)
    block_green(t,x,y)

    score_blue()
    score_green()

total = 0
for r in range(6):
    total += sum(GREEN[r])

for r in range(4):
    for c in range(6):
        total += BLUE[r][c]

print(score)
print(total)