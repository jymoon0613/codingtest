# 17779: 게리맨더링 2

import sys

input = sys.stdin.readline

n = int(input())

total = 0
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    total += sum(array[i])

result = int(1e+9)
def get_score(x,y,d1,d2):

    global result

    g1 = 0
    col = y+1
    for r in range(x+d1):
        if r >= x:
            col -= 1
        for c in range(col):
            g1 += array[r][c]

    g2 = 0
    col = y+1
    for r in range(x+d2+1):
        if r > x:
            col += 1
        for c in range(col, n):
            g2 += array[r][c]

    g3 = 0
    col = y-d1
    for r in range(x+d1, n):
        for c in range(col):
            g3 += array[r][c]
        if r < (x+d1+d2):
            col += 1

    g4 = 0
    col = y + d2
    for r in range(x+d2+1, n):
        for c in range(col, n):
            g4 += array[r][c]
        if r <= (x+d1+d2):
            col -= 1

    g5 = total - (g1+g2+g3+g4)

    result = min(result, max(g1, g2, g3, g4, g5)-min(g1,g2,g3,g4,g5))


for x in range(n-2):
    for y in range(1, n-1):
        for d1 in range(1,n-1):
            for d2 in range(1,n-1):
                if (x+d1+d2) < n and (y+d2) < n:
                    get_score(x,y,d1,d2)

print(result)