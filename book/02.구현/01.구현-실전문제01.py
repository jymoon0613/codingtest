# 왕실의 나이트

## 나의 답안 ##

s = input()

dx = [-2, -2, 2, 2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

result = 0
for i in range(8):

    nx = (ord(s[0]) - ord('a')) + dx[i]
    ny = (int(s[1]) - 1) + dy[i]
    
    if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
        result += 1

print(result)

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