# 2785: 체인

n = int(input())

num = list(map(int, input().split()))

num.sort()

i = 0
j = (n-1)
result = 0
while True:

    num[i] -= 1
    j -= 1
    result += 1

    if num[i] == 0:
        i += 1

    if i >= j:
        break

print(result)