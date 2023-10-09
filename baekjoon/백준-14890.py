# 14890: 경사로

import sys

input = sys.stdin.readline

n, l = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

result = 0
def search():

    global result
    
    for x in range(n):
        row = array[x]
        accum = 1
        prev = row[0]
        possible = True
        for y in range(1,n):
            if row[y] == prev:
                accum += 1
            elif row[y] > prev:
                if (row[y] - prev) >= 2 or accum < l:
                    possible = False
                    break
                else:
                    prev = row[y]
                    accum = 1
            else:
                if (prev - row[y]) >= 2:
                    possible = False
                    break
                accum_temp = 1
                for yy in range(y+1, n):
                    if row[yy] == row[y]:
                        accum_temp += 1
                    else:
                        break
                if accum_temp < l:
                    possible = False
                    break
                else:
                    prev = row[y]
                    accum = -l+1

        if possible:
            result += 1

search()
array = list(map(list, zip(*array)))
search()
print(result)