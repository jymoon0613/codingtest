# 13164: 행복 유치원

n, k = map(int, input().split())

pos = list(map(int, input().split()))

dist = []
for i in range(n-1):
    dist.append((pos[i+1] - pos[i]))

dist.sort()
for _ in range(k-1):
    dist.pop()

result = sum(dist)

print(result)