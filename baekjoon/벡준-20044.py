# 20044: Project Teams

from collections import deque

n = int(input())

ws = deque(sorted(list(map(int, input().split()))))

result = int(1e+9)
for i in range(n):
    l = ws.popleft()
    r = ws.pop()
    result = min(result, l+r)

print(result)