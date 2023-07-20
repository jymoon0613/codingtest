# 퇴사

## 나의 답안 ##

n = int(input())
array = []
for _ in range(n):
    t, p = map(int, input().split())
    array.append((t, p))
    
dp = [0] * (n+1)
max_value = 0
for i in range(n-1, -1, -1):
    ti, pi = array[i]
    tn = i + ti
    if tn <= n:
        dp[i] = max(pi + dp[tn], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
        
print(max(dp))

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