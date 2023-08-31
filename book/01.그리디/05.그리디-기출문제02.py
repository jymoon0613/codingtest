# 곱하기 혹은 더하기

## 나의 답안 ##

array = list(map(int, input()))

result = array[0]
for i in range(1, len(array)):
    if result <= 1 or array[i] <= 0:
        result += array[i]
    else:
        result *= array[i]

print(result)

## 예시 답안 ##

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else :
        result *= num

print(result)