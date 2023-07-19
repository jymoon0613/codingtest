# 정수 삼각형

## 나의 답안 ##

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
    
result = []
result.append(array[0])
for i in range(len(array)-1):
    
    l = len(array[i]) + 1
    r = []
    
    for j in range(l):
        if j == 0:
            r.append(result[i][j] + array[i+1][j])
        elif j == (l-1):
            r.append(result[i][j-1] + array[i+1][j])
        else:
            left = result[i][j-1] + array[i+1][j]
            right = result[i][j] + array[i+1][j]
            r.append(max(left, right))
            
    result.append(r)
    
print(max(result[-1]))

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