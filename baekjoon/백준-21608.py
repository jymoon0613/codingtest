# 21608: 상어 초등학교

import sys

input = sys.stdin.readline

n = int(input())

array = [[0] * n for _ in range(n)]

like_dict = {}
for _ in range(n*n):
    data = list(map(int, input().split()))
    like_dict[data[0]] = data[1:]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_position(like):

    result = []
    for x in range(n):
        for y in range(n):
            if array[x][y] == 0:
                cnt_like = 0
                cnt_zero = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        if array[nx][ny] in like:
                            cnt_like += 1
                        elif array[nx][ny] == 0:
                            cnt_zero += 1
                        else:
                            continue
                result.append((cnt_like, cnt_zero, x, y))

    result.sort(key=lambda x: -x[0])
    max_like = result[0][0]
    result = [x for x in result if x[0] >= max_like]

    if len(result) > 1:
        result.sort(key=lambda x: -x[1])
        max_zero = result[0][1]
        result = [x for x in result if x[1] >= max_zero]

    if len(result) > 1:
        result.sort(key=lambda x: x[2])
        min_row = result[0][2]
        result = [x for x in result if x[2] <= min_row]

    if len(result) > 1:
        result.sort(key=lambda x: x[3])
        min_col = result[0][3]
        result = [x for x in result if x[3] <= min_col]

    return result[0][2:]

def get_score():
    result = 0
    for x in range(n):
        for y in range(n):
            l = like_dict[array[x][y]]
            cnt = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if array[nx][ny] in l:
                        cnt += 1
            if cnt != 0:
                result += (10 ** (cnt-1))
            else:
                continue

    return result

for index in like_dict.keys():
    like = like_dict[index]
    x, y = get_position(like)
    array[x][y] = index

print(get_score())