# 큰 수의 법칙

## 나의 답안 ##

n, m, k = map(int, input().split())

array = list(map(int, input().split()))

array.sort(reverse=True)

num1 = array[0]
num2 = array[1]

result = (m // (k + 1)) * (num1 * k + num2) + (m % (k + 1)) * num1

print(result)

## 예시 답안 1 ##

n, m, k = list(map(int, input().split()))

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:

    for i in range(k):
        if m == 0:
            break
        result += first
        m -=1

    if m == 0:
        break

    result += second
    m -= 1

print(result)

## 예시 답안 2 ##

n, m, k = list(map(int, input().split()))

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)