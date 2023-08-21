# 위에서 아래로

## 나의 답안 ##

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in range(len(array)):
    print(array[i], end=' ')

## 예시 답안 ##

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')