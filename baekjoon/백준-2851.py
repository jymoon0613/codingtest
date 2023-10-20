# 2851: 슈퍼 마리오

mush = []
for _ in range(10):
    mush.append(int(input()))

dp = [0] * 11
dist = [0] * 11
dist[0] = 100

target = 100
for i in range(10):
    dp[i+1] = dp[i] + mush[i]
    dist[i+1] = abs(target-dp[i+1])

min_dist = int(1e+9)
result = 0
for i in range(11):
    if dist[i] <= min_dist:
        min_dist = dist[i]
        result = dp[i]

print(result)