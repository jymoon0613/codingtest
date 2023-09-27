# 13458: 시험 감독

n = int(input())

a = list(map(int, input().split()))

b, c = map(int, input().split())

result = 0
for i in range(n):

    result += 1
    a[i] -= b

    if a[i] > 0:
        num = a[i] // c
        result += num
        a[i] -= (num * c)

    if a[i] > 0:
        result += 1

print(result)