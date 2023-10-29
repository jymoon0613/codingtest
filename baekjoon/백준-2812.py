# 2812: 크게 만들어

n, k = map(int, input().split())
num = input()

res = []
for i in range(n):
    while res and int(res[-1]) < int(num[i]) and k > 0:
        res.pop()
        k -= 1
    res.append(num[i])

if k > 0:
    result = int(''.join(res[:-k]))
else:
    result = int(''.join(res))

print(result)