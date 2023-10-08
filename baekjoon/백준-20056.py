# 20056: 마법사 상어와 파이어볼

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

array = [[[] for _ in range(n)] for _ in range(n)]

balls = []
for _ in range(m):
    x, y, z, s, d = map(int, input().split())
    balls.append((x, y, z, s, d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):

    while balls:
        x, y, z, s, d = balls.pop(0)
        nx = (x + s * dx[d]) % n
        ny = (y + s * dy[d]) % n
        array[nx][ny].append((z,s,d))

    for x in range(n):
        for y in range(n):
            if len(array[x][y]) >= 2:
                sum_z, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(array[x][y])
                while array[x][y]:
                    z, s, d = array[x][y].pop(0)
                    sum_z += z
                    sum_s += s
                    if d % 2 == 0:
                        cnt_odd += 1
                    else:
                        cnt_even += 1

                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]
                if (sum_z // 5) != 0:
                    for d in nd:
                        balls.append((x, y, sum_z // 5, sum_s // cnt, d))

            if len(array[x][y]) == 1:
                z, s, d = array[x][y].pop(0)
                balls.append((x, y, z, s, d))
                
result = 0
for ball in balls:
    result += ball[2]

print(result)