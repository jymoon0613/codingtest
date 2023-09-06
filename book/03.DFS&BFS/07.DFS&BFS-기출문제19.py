# 연산자 끼워 넣기

## 나의 답안 ##

n = int(input())

a = list(map(int, input().split()))

oper = list(map(int, input().split()))

max_value = -int(1e+9)
min_value = int(1e+9)
def dfs(value, ind):

    global max_value, min_value

    if ind >= n:
        max_value = max(max_value, value)
        min_value = min(min_value, value)

    else:
        if oper[0] != 0:
            oper[0] -= 1
            dfs(value + a[ind], ind+1)
            oper[0] += 1
            
        if oper[1] != 0:
            oper[1] -= 1
            dfs(value - a[ind], ind+1)
            oper[1] += 1

        if oper[2] != 0:
            oper[2] -= 1
            dfs(value * a[ind], ind+1)
            oper[2] += 1

        if oper[3] != 0:
            oper[3] -= 1
            dfs(int(value / a[ind]), ind+1)
            oper[3] += 1

dfs(a[0], 1)

print(max_value)
print(min_value)

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