# 왕실의 나이트

x = list(input())

row = int(x[1])
col = int(ord(x[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

res = 0
for step in steps:
    row_next = row + step[0]
    col_next = col + step[1]

    if row_next >= 1 and row_next <= 8 and col_next >= 1 and col_next <= 8:
        res += 1

print(res)

