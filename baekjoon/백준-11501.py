# 11501: 주식

t = int(input())
for _ in range(t):

    n = int(input())
    price = list(map(int, input().split()))
    price = price[::-1]
    result = 0
    ref = price[0]
    for i in range(1, n):
        if ref > price[i]:
            result += (ref - price[i])
        else:
            ref = price[i]

    print(result)