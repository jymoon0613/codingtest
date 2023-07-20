# 병사 배치하기

## 나의 답안 ##

n = int(input())

array = list(map(int, input().split()))

dp = [0] * n
dp[0] = array[0]

cnt = 0
for i in range(1, n):
    if array[i] < dp[i-1]:
        dp[i] = array[i]
    else:
        dp[i] = array[i]
        cnt += 1
        
print(cnt)

## 예시 답안 ##

n = int(input())

array = list(map(int, input().split()))

array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
        
print(n-max(dp))
        