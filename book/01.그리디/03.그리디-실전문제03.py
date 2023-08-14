# 1이 될 때까지

## 나의 답안 ##

n, k = map(int, input().split())

cnt = 0
while n != 1:
    if n % k == 0:
        n /= k

    else:
        n -= 1

    cnt += 1

print(cnt)

## 예시 답안 1 ##

n, k = map(int, input().split())
result = 0

while n >= k:
    if n % k != 0:
        n -= 1
        result += 1

    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

## 예시 답안 2 ##

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n-1)
print(result)