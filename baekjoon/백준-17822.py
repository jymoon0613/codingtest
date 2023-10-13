# 17822: 원판 돌리기

import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())

array = []
for _ in range(n):
    array.append(deque(list(map(int, input().split()))))

rotations = [list(map(int, input().split())) for _ in range(t)]

def rotate_array(x, d, k):
    for i in range(n):
        if (i+1) % x == 0:
            for _ in range(k):
                if d == 0:
                    a = array[i].pop()
                    array[i].appendleft(a)
                else:
                    a = array[i].popleft()
                    array[i].append(a)

def remove_array():
    remove_inds = []
    for i in range(n):
        for j in range(m):
            if array[i][j] != 'x':
                for k in [1,-1]:
                    jj = (j+k) % m
                    if array[i][jj] == array[i][j]:
                        remove_inds.append((i,jj))
                        remove_inds.append((i,j))
                if i == 0:
                    if array[i][j] == array[i+1][j]:
                        remove_inds.append((i,j))
                        remove_inds.append((i+1,j))
                elif i == (n-1):
                    if array[i][j] == array[i-1][j]:
                        remove_inds.append((i,j))
                        remove_inds.append((i-1,j))
                else:
                    if array[i][j] == array[i-1][j]:
                        remove_inds.append((i,j))
                        remove_inds.append((i-1,j))
                    if array[i][j] == array[i+1][j]:
                        remove_inds.append((i,j))
                        remove_inds.append((i+1,j))

    remove_inds = set(remove_inds)

    if len(remove_inds) == 0:
        total, cnt = get_score()
        if cnt != 0:
            for i in range(n):
                for _ in range(m):
                    a = array[i].popleft()
                    if a != 'x':
                        if a > (total / cnt):
                            array[i].append(a-1)
                        elif a < (total / cnt):
                            array[i].append(a+1)
                        else:
                            array[i].append(a)                    
                    else:
                        array[i].append(a)
                
    else:
        for inds in remove_inds:
            i,j = inds
            array[i][j] = 'x'

def get_score():
    result = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] != 'x':
                result += array[i][j]
                cnt += 1
    
    return result, cnt

for rotation in rotations:

    x, d, k = rotation

    rotate_array(x, d, k)

    remove_array()

result, _ = get_score()

print(result)