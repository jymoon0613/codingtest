# 17837: 새로운 게임 2

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

horse = [[deque() for _ in range(n)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(k):
    a, b, c = map(int, input().split())
    horse[a-1][b-1].append((i+1, c-1))

def get_horse_position(index):
    for x in range(n):
        for y in range(n):
            if len(horse[x][y]) != 0:
                for i in range(len(horse[x][y])):
                    if horse[x][y][i][0] == index:
                        return (x, y, horse[x][y][i][1])
                    
def check():
    for x in range(n):
        for y in range(n):
            if len(horse[x][y]) >= 4:
                return True
    return False
                    
cnt = 0
def move_horse():
    for index in range(1, k+1):
        x, y, d = get_horse_position(index)
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or array[nx][ny] == 2:
            if d in [0,2]:
                d += 1
            else:
                d -= 1
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or array[nx][ny] == 2:
                for _ in range(len(horse[x][y])):
                    item = horse[x][y].popleft()
                    if item[0] == index:
                        new_item = (index, d)
                        horse[x][y].append(new_item)
                    else:
                        horse[x][y].append(item)

            else:
                if array[nx][ny] == 0:
                    detect=False
                    for _ in range(len(horse[x][y])):
                        item = horse[x][y].popleft()
                        if item[0] == index:
                            detect = True
                        if detect:
                            if item[0] == index:
                                new_item = (index, d)
                                horse[nx][ny].append(new_item)
                            else:
                                horse[nx][ny].append(item)
                        else:
                            horse[x][y].append(item)
                else:
                    for i in range(len(horse[x][y])):
                        item = horse[x][y].pop()
                        horse[nx][ny].append(item)
                        if item[0] == index:
                            item = horse[nx][ny].pop()
                            horse[nx][ny].append((index, d))
                            break

        elif array[nx][ny] == 0:
            detect=False
            for i in range(len(horse[x][y])):
                item = horse[x][y].popleft()
                if item[0] == index:
                    detect = True
                if detect:
                    horse[nx][ny].append(item)
                else:
                    horse[x][y].append(item)

        else:
            for i in range(len(horse[x][y])):
                item = horse[x][y].pop()
                horse[nx][ny].append(item)
                if item[0] == index:
                    break

        ch = check()

        if ch:
            return False

    return True

while True:

    possible = move_horse()

    cnt += 1

    if not possible or cnt > 1000:
        break

if cnt > 1000:
    print(-1)
else:
    print(cnt)