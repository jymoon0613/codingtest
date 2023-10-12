# 12100: 2048 (Easy)

import sys
import copy

input = sys.stdin.readline

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

def move_block(array, d=0):
    
    temp = [[0] * n for _ in range(n)]

    # 상
    if d == 0:
        inds = [0] * n
        for x in range(n):
            for y in range(n):
                if array[x][y] != 0:
                    for row in range(x+1,n):
                        if array[row][y] == 0:
                            continue
                        elif array[x][y] != array[row][y]:
                            break
                        else:
                            array[x][y] += array[row][y]
                            array[row][y] = 0
                            break
                if array[x][y] != 0:
                    temp[inds[y]][y] = array[x][y]
                    inds[y] += 1

    # 하
    elif d == 1:
        inds = [-1] * n
        for x in range(n-1, -1, -1):
            for y in range(n):
                if array[x][y] != 0:
                    for row in range(x-1,-1, -1):
                        if array[row][y] == 0:
                            continue
                        elif array[row][y] != array[x][y]:
                            break
                        else:
                            array[x][y] += array[row][y]
                            array[row][y] = 0
                            break

                    temp[inds[y]][y] = array[x][y]
                    inds[y] -= 1

    # 좌               
    elif d == 2:
        inds = [0] * n
        for x in range(n):
            for y in range(n):
                if array[x][y] != 0:
                    for col in range(y+1,n):
                        if array[x][col] == 0:
                            continue
                        elif array[x][y] != array[x][col]:
                            break
                        else:
                            array[x][y] += array[x][col]
                            array[x][col] = 0
                            break

                    temp[x][inds[x]] = array[x][y]
                    inds[x] += 1
    
    # 우
    else:    
        inds = [-1] * n
        for x in range(n):
            for y in range(n-1,-1,-1):
                if array[x][y] != 0:
                    for col in range(y-1,-1,-1):
                        if array[x][col] == 0:
                            continue
                        elif array[x][y] != array[x][col]:
                            break
                        else:
                            array[x][y] += array[x][col]
                            array[x][col] = 0
                            break

                    temp[x][inds[x]] = array[x][y]
                    inds[x] -= 1

    return temp

result = 0
def search(array, cnt):

    global result

    if cnt == 5:
        for x in range(n):
            for y in range(n):
                if array[x][y] != 0:
                    result = max(result, array[x][y])
        return

    else:
        for i in range(4):
            temp = copy.deepcopy(array)
            search(move_block(temp, d=i), cnt+1)

search(array,0)
print(result)