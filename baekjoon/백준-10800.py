# 10800: 컬러볼

import sys

input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    c, s = map(int, input().split())
    array.append((c,s,i))

array.sort(key=lambda x: x[1])

result = [0] * (n+1)
total_size = [0] * (n+1)

total = 0
j = 0
for i in range(n):
    while array[j][1] < array[i][1]:
        total += array[j][1]
        total_size[array[j][0]] += array[j][1]
        j += 1
    result[array[i][2]] = total - total_size[array[i][0]]

for i in range(n):
    print(result[i])