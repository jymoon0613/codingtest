# 왕실의 나이트

## 나의 답안 ##

p = input()

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

rows = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
cols = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

col, row = p[0], p[1]

cnt = 0
for i in range(len(dx)):
    nx = cols[col] + dx[i]
    ny = rows[row] + dy[i]

    if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
        cnt += 1

print(cnt)

## 예시 답안 ##

input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

res = 0
for step in steps:
    next_row = row + step[0]
    next_col = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        res += 1

print(res)