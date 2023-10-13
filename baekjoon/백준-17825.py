# 17825: 주사위 윷놀이

import sys
import copy

input = sys.stdin.readline

numbers = list(map(int, input().split()))

graph = [
    [1], [2], [3], [4], [5], 
    [6, 21], [7], [8], [9], [10],
    [11, 24], [12], [13], [14], [15],
    [16, 26], [17], [18], [19], [20],
    [32], [22], [23], [29], [25], 
    [29], [27], [28], [29], [30], 
    [31], [20], [32]
]

MAP = [
    0,  2,  4,  6,  8, 
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28, 
    30, 32, 34, 36, 38, 
    40, 13, 16, 19, 22, 
    24, 28, 27, 26, 25,
    30, 35, 0
]

horse = [0] * 4
result = 0
def dfs(horse, cnt, value):

    global result

    if cnt == 10:
        result = max(result, value)
        return
    else:
        for i in range(4):
            x = horse[i]

            if len(graph[x]) == 2:
                x = graph[x][1]
            else:
                x = graph[x][0]

            for _ in range(1, numbers[cnt]):
                x = graph[x][0]

            if x == 32 or (x < 32 and x not in horse):
                before = horse[i]

                horse[i] = x

                dfs(horse, cnt+1, value+MAP[x])

                horse[i] = before

dfs(horse, 0, 0)

print(result)