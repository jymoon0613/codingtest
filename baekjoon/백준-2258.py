# 2258: 정육점

n, m = map(int, input().split())

array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, b))

array.sort(key=lambda x: (x[1], -x[0]))

def solution():

    total, same = 0, 0
    possible = False
    result = 2147483647

    for i in range(n):
        total += array[i][0]
        if i >= 1 and array[i][1] == array[i-1][1]:
            same += array[i][1]
        else:
            same = 0
        if total >= m:
            result = min(result, array[i][1] + same)
            possible = True

    if possible:
        print(result)
    else:
        print(-1)

solution()