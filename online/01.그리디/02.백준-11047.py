# 11047: 동전 0

n, k = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

result = 0
for i in range(n-1, -1, -1):
    if array[i] <= k:
        result += (k // array[i])
        k %= array[i]

    if k == 0:
        break

print(result)