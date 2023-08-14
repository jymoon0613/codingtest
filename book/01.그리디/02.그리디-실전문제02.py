# 숫자 카드 게임

## 나의 답안 ##

n, m = map(int, input().split())

max_num = -1
for i in range(n):
    data = list(map(int, input().split()))
    min_num = int(1e+9)
    for j in range(m):
        if data[j] < min_num:
            min_num = data[j]


    if min_num > max_num:
        max_num = min_num

print(max_num)

## 예시 답안 ##

n, m = list(map(int, input().split()))

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)

    result = max(result, min_value)
        
print(result)