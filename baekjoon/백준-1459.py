# 1459: 걷기

from collections import deque
import copy

x, y, w, s = map(int, input().split())

res1 = (x + y) * w

if (x + y) % 2 == 0:
    res2 = max(x,y) * s
else:
    res2 = (max(x,y) - 1) * s + w

res3 = (min(x,y) * s) + ((max(x,y) - min(x,y)) * w)

result = min(res1, res2, res3)

print(result)