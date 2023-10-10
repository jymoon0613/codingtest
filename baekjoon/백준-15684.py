# 15684: 사다리 조작

import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())

array = [[0] * (n+1) for _ in range(h+1)]

for _ in range(m):
    a, b = map(int, input().split())
    array[a][b] = 1

def check():

    for y in range(1,n+1):
        start = y
        for x in range(1, h+1):
            if array[x][y] == 1:
                y += 1
            elif (y-1) >= 1 and array[x][y-1] == 1:
                y -= 1
        if start != y:
            return False

    return True

result = 4
def dfs(cnt, x, y):

    global result

    if check():
        result = min(result, cnt)
        return
    elif cnt >= 3 or cnt >= result:
        return

    for i in range(x, h+1):
        if i == x:
            now = y
        else:
            now = 0
        for j in range(now, n):
            if array[i][j] != 1 and array[i][j+1] != 1 and array[i][j-1] != 1:
                array[i][j] = 1
                dfs(cnt+1, i, j)
                array[i][j] = 0

dfs(0, 1, 1)

print(result if result < 4 else -1)