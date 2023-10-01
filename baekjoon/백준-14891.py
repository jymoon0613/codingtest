# 14891: 톱니바퀴

import sys
from collections import deque

input = sys.stdin.readline

array = [deque(list(map(int, input().rstrip()))) for _ in range(4)]

k = int(input())

rotation = []
for _ in range(k):
    n, d = map(int, input().split())
    rotation.append((n,d))

def rotate_one(index, direction):

    if direction == 1:
        x = array[index].pop()
        array[index].appendleft(x)
    else:
        x = array[index].popleft()
        array[index].append(x)

def get_score():

    score = 0
    weight = 1
    for i in range(4):
        score += (weight * array[i][0])
        weight *= 2

    return score

def check_rotations():

    if array[0][2] != array[1][6]:
        r1 = True
    else:
        r1 = False

    if array[1][2] != array[2][6]:
        r2 = True
    else:
        r2 = False

    if array[2][2] != array[3][6]:
        r3 = True
    else:
        r3 = False

    return r1, r2, r3

for index, direction in rotation:

    rs = check_rotations()

    rotate_one(index-1, direction)

    if index == 1:
        d = -direction
        for i in range(3):
            if rs[i]:
                rotate_one(i+1, d)
                d = -d
            else:
                break

    elif index == 2:
        d = -direction
        if rs[0]:
            rotate_one(0, d)

        d = -direction
        for i in range(1,3):
            if rs[i]:
                rotate_one(i+1, d)
                d = -d
            else:
                break

    elif index == 3:
        d = -direction
        if rs[2]:
            rotate_one(3, d)

        d = -direction
        for i in range(1, -1, -1):
            if rs[i]:
                rotate_one(i, d)
                d = -d
            else:
                break

    else:
        d = -direction
        for i in range(2, -1, -1):
            if rs[i]:
                rotate_one(i, d)
                d = -d
            else:
                break

result = get_score()

print(result)