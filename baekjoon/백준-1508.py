# 1508: 레이스

import heapq

n, m, k = map(int, input().split())

pos = list(map(int, input().split()))

def check(x):
    now = -1
    cnt = 0
    for i in range(k):
        if now <= pos[i]:
            cnt += 1
            now = pos[i] + x
    if cnt < m:
        return False
    return True

start = 0
end = pos[-1] + 1
while (start + 1) < end:
    mid = (start + end) // 2
    if check(mid):
        start = mid
    else:
        end = mid

result = ''
now = 0
cnt = 0
for i in range(k):
    if now <= pos[i] and cnt < m:
        result += '1'
        now = pos[i] + start
        cnt += 1
    else:
        result += '0'

print(result)