# 위에서 아래로

## 나의 답안 ##

N = int(input())

data = []
for _ in range(N):
    data.append(int(input()))

data.sort(reverse=True)

for d in data:
    print(d, end=' ')

## 예시 답안 ##

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in data:
    print(i, end=' ')