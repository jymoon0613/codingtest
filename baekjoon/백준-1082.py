# 방 번호

n = int(input())
p = list(map(int, input().split()))
m = int(input())

INF = int(1e+9)

dp = [-INF] * (m+1)
for i in range(n-1, -1, -1):
    p_ = p[i]
    for j in range(p_, m+1):
        dp[j] = max(dp[j-p_]*10+i, i, dp[j])

print(dp[m])