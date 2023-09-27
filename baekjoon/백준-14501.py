# 13458: 퇴사

n = int(input())

t = []
p = []

dp = [0] * (n+1)

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

max_value = 0
for i in range(n-1, -1, -1):
    
    end = i + t[i]

    if end <= n:
        dp[i] = max(max_value, p[i] + dp[end])
        max_value = dp[i]

    else:
        dp[i] = max_value

print(max_value)