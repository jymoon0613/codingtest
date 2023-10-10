# 15685: 드래곤 커브

import sys

input = sys.stdin.readline

n = int(input())

array = [[False] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

curves = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
    curves.append((x,y,d,g))

for curve in curves:
    x, y, d, g = curve

    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            nd = (move[-i-1] + 1) % 4
            temp.append(nd)
        move.extend(temp)

    array[y][x] = True
    for d in move:
        x += dx[d]
        y += dy[d]
        if x >= 0 and x <=100 and y >= 0 and y <= 100:
            array[y][x] = True

result = 0
for y in range(100):
    for x in range(100):
        if array[y][x] and array[y][x+1] and array[y+1][x+1] and array[y+1][x]:
            result += 1

print(result)