# 금광

## 나의 답안 ##

t = int(input())

for _ in range(t):

    n, m = map(int, input().split())

    array = list(map(int, input().split()))

    result = []
    for i in range(0, len(array), m):
        res = 0
        visited = [0] * len(array)
        cnt = 0
        while True:     
            mi = -1
            res += array[i]
            pi = i
            visited[i] = 1
            if (pi-(m-1)) >= 0 and (pi-(m-1)) < len(array) and visited[pi-(m-1)] != 1:
                if mi < array[pi-(m-1)]:
                    mi = array[pi-(m-1)]
                    i = pi-(m-1)
            if (pi+1) >= 0 and (pi+1) < len(array) and visited[pi+1] != 1:
                if mi < array[pi+1]:
                    mi = array[pi+1]
                    i = pi+1           
            if (pi+(m+1)) >= 0 and (pi+(m+1)) < len(array) and visited[pi+(m+1)] != 1:
                if mi < array[pi+(m+1)]:
                    mi = array[pi+(m+1)]
                    i = pi+(m+1)
                    
            cnt += 1
            
            if mi == -1 or cnt == m:
                break

        result.append(res)

    print(max(result))

## 예시 답안 ##

for tc in range(int(input())):

    n, m = map(int, input().split())

    array = list(map(int, input().split()))
    
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
        
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
                
            else:
                left_up = dp[i-1][j-1]
                
            if i == n - 1:
                left_down = 0
            
            else:
                left_down = dp[i+1][j-1]
                
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
            
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)