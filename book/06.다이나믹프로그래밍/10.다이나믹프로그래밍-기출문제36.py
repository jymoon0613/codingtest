# 편집 거리

## 나의 답안 ##

a = input()
b = input()

d = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    d[i][0] = i
    for j in range(1, len(b)+1):
        d[0][j] = j

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            d[i][j] = d[i-1][j-1]
        else:
            insert = d[i][j-1] + 1
            delete = d[i-1][j] + 1
            replace = d[i-1][j-1] + 1
            d[i][j] = min(insert, delete, replace)

print(d[len(a)][len(b)])

## 예시 답안 ##

def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                
    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))