# 연산자 끼워 넣기

## 나의 답안 ##

n = int(input())

a = list(map(int, input().split()))

add, sub, mul, div = list(map(int, input().split()))

mini = int(1e9)
maxi = int(-1e9)

def solution(ind, now):

    global a, add, sub, mul, div, mini, maxi

    if ind == n:
        mini = min(mini, now)
        maxi = max(maxi, now)

    if add >= 1:
        add -= 1
        solution(ind+1, now + a[ind])
        add += 1
    if sub >= 1:
        sub -= 1
        solution(ind+1, now - a[ind])
        sub += 1
    if mul >= 1:
        mul -= 1
        solution(ind+1, now * a[ind])
        mul += 1
    if div >= 1:
        div -= 1
        solution(ind+1, int(now / a[ind]))
        div += 1

solution(1, a[0])
print(maxi)
print(mini)

## 예시 답안 ##

n = int(input())

data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
        
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/data[i]))
            div += 1

dfs(1, data[0])
print(max_value)
print(min_value)