# 17140: 이차원 배열과 연산

import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(3)]

def operation_r(array):

    max_len = 0
    row_count = [[] for _ in range(len(array))]
    for x in range(len(array)):
        prev = []
        for y in range(len(array[0])):
            if array[x][y] != 0 and array[x][y] not in prev:
                count = array[x].count(array[x][y])
                row_count[x].append((array[x][y], count))
                prev.append(array[x][y])

        row_count[x].sort(key=lambda x: (x[1], x[0]))
        max_len = max(len(row_count[x]) * 2, max_len)

    max_len = min(max_len, 100)

    new_array = [[] for _ in range(len(array))]

    for x in range(len(array)):
        row = row_count[x]
        if len(row) * 2 < max_len:
            need = max_len - (len(row) * 2)
            for _ in range(0, need, 2):
                row.append((0,0))
        
        for tu in row:
            new_array[x].append(tu[0])
            new_array[x].append(tu[1])

    return new_array

def operation_c(array):

    array = list(map(list, zip(*array)))

    new_array = operation_r(array)

    new_array = list(map(list, zip(*new_array)))

    return new_array

t = 0
result = -1
while True:

    if t > 100:
        break

    if len(array) >= r and len(array[0]) >= c and array[r-1][c-1] == k:
        result = t
        break
    
    if len(array) >= len(array[0]):
        array = operation_r(array)
    else:
        array = operation_c(array)

    t += 1

print(result)