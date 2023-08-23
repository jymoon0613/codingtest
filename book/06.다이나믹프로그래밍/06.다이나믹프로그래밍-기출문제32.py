# 정수 삼각형

## 나의 답안 ##

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

d = [[0] * i for i in range(1,n+1)]

d[0][0] = array[0][0]

result = -1

for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0:
            left = 0
        else:
            left = d[i-1][j-1]
        if j == (len(d[i]) - 1):
            right = 0
        else:
            right = d[i-1][j]

        d[i][j] = array[i][j] + max(left, right)
        result = max(result, d[i][j])

print(result)

## 예시 답안 ##

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]

        if j == i:
            up = 0
        else:
            up = dp[i-1][j]

        dp[i][j] = dp[i][j] + max(up_left, up)
    
print(max(dp[n-1]))