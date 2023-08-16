# 치킨 배달

## 나의 답안 ##

from itertools import combinations

def cal(candidate, hs):
    result = []
    for i in range(len(hs)):
        hx, hy = hs[i]
        m = int(1e+9)
        for cx, cy in candidate:
            diff = abs(hx - cx) + abs(hy - cy)
            if diff < m:
                m = diff

        result.append(m)

    return sum(result)

n, m = map(int, input().split())

hs = []
cs = []
for i in range(n):
    array = list(map(int, input().split()))
    for j in range(n):
        if array[j] == 1:
            hs.append((i, j))
        elif array[j] == 2:
            cs.append((i, j))
        else:
            continue

candidates = combinations(cs, m)

res = []
for candidate in candidates:

    res.append(cal(candidate, hs))

print(min(res))

## 예시 답안 ##

from itertools import combinations

n, m = map(int, input().split())

chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))
            
candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
            
        result += temp
        
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
    
print(result)