# 병사 배치하기

## 나의 답안 ##

n = int(input())

array = list(map(int, input().split()))

array.reverse()

d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j]+1)

print(d)
print(n - max(d))

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
        