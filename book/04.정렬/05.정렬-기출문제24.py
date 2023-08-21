# 안테나

## 나의 답안 ##

n = int(input())
array = list(map(int, input().split()))

array.sort()

ind = int((len(array) - 1) / 2)

print(array[ind])

## 예시 답안 ##

n = int(input())

data = list(map(int, input().split()))

data.sort()

print(data[(n-1) // 2])