# 1398: 동전 문제

t = int(input())
coin = [1, 10, 25]

for i in range(t):
    num = int(input())
    result = 0
    dp = [10**15+1 for _ in range(100)]
    dp[0] = 0
    for c in coin:
        for i in range(c, 100):
            dp[i] = min(dp[i], dp[i-c]+1)
    while num:
        result += dp[num%100]
        num //= 100
    print(result)