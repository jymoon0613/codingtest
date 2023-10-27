# 2012: 등수 매기기

import sys

input = sys.stdin.readline

n = int(input())

pos = [int(input()) for _ in range(n)]

pos.sort()

result = 0
for i in range(n):
    result += abs((i+1) - pos[i])

print(result)