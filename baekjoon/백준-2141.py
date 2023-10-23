# 2141: 우체국

n = int(input())

total = 0
XA = []
for _ in range(n):
    x, a = map(int, input().split())
    XA.append((x,a))
    total += a

XA.sort()

now = 0
for i in range(n):
    now += XA[i][1]
    if now >= total / 2:
        print(XA[i][0])
        break