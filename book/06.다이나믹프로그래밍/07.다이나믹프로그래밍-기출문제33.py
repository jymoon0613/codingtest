# 퇴사

## 나의 답안 ##

n = int(input())

ts = []
ps = []
for _ in range(n):
    t, p = map(int, input().split())
    ts.append(t)
    ps.append(p)

d = [0] * (n+1)

maxi = 0
for i in range(n-1, -1, -1):
    t, p = ts[i], ps[i]
    end = i + t

    if end > n:
        d[i] = maxi
    else:
        d[i] = max(p + d[end], maxi)
        maxi = d[i]

print(max(d))

## 예시 답안 ##

n = int(input())
t = []
p = []
dp = [0] * (n+1)
max_value = 0
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
        
    else:
        dp[i] = max_value
        
print(max_value)