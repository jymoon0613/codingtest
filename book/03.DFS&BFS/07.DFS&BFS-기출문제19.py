# 연산자 끼워 넣기

## 나의 답안 ##

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
nP, nM, nT, nD = map(int, input().split())

operators = []
for _ in range(nP):
    operators.append('+')

for _ in range(nM):
    operators.append('-')
    
for _ in range(nT):
    operators.append('*')
    
for _ in range(nD):
    operators.append('/')
    
candidates = list(permutations(operators, N-1))

result = []

res = 0
for candidate in candidates:
    for i in range(len(A)-1):
        operator = candidate[i]
        if operator == '+':
            if i == 0:
                res = A[i] + A[i+1]
            else:
                res = res + A[i+1]
        elif operator == '-':
            if i == 0:
                res = A[i] - A[i+1]
            else:
                res = res - A[i+1]
        elif operator == '*':
            if i == 0:
                res = A[i] * A[i+1]
            else:
                res = res * A[i+1]
        else:
            if i == 0:
                if A[i] < 0:
                    res = -(abs(A[i]) // A[i+1])
                else:
                    res = A[i] // A[i+1]
            else:
                if res < 0 :
                    res = -(abs(res) // A[i+1])
                else:
                    res = res // A[i+1]
                    
    result.append(res)
    
print(max(result), min(result), sep='\n')

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