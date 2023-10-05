# 1025: 제곱수 찾기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(input().rstrip()) for _ in range(n)]

def check(num):
    num = int(num)
    return int(num**0.5)**2 == num

result = -1
for x in range(n):
    for y in range(m):
        for step_x in range(-n,n):
            for step_y in range(-m,m):
                num = ''
                nx, ny = x, y
                if step_x == 0 and step_y == 0:
                    continue
                else:
                    while nx >= 0 and nx < n and ny >= 0 and ny < m:
                        num += array[nx][ny]
                        if check(num):
                            result = max(result, int(num))
                        nx += step_x
                        ny += step_y

print(result)