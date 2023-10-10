# 15685: 드래곤 커브

# import sys

# input = sys.stdin.readline

# n = int(input())

# curves = []
# for _ in range(n):
#     x, y, d, g = map(int, input().split())
#     curves.append((x,y,d,g))

# array = [[0] * 100 for _ in range(100)]

# result = []

# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]

# d = 0

# sx, sy = 1, 1
# ex, ey = sx+dx[d], sy+dx[y]

# result.append((sx,sy))
# result.append((ex,ey))

# print(result)

# start = 0
# while start < g:

#     pass

l = [(0,0), (1,0)]

a = []
for line in l:
    x, y = line
    a.append((x+1,y-1))

print(a)