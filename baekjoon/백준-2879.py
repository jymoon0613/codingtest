# 2879: 코딩은 예쁘게

from collections import deque

n = int(input())

now = list(map(int, input().split()))
target = list(map(int, input().split()))

result = 0
check = 0
while now != target:
    for i in range(n):
        if now[i] == target[i]:
            check = 0
        elif now[i] > target[i]:
            if check != 1:
                result += 1
                now[i] -= 1
                check = 1
            else:
                now[i] -= 1
        else:
            if check != 2:
                result += 1
                now[i] += 1
                check = 2
            else:
                now[i] += 1
    check = 0

print(result)