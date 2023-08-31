# 숫자 카드 게임

## 나의 답안 ##

n, m = map(int, input().split())

max_value = -1
for i in range(n):
    row = list(map(int, input().split()))
    min_value = min(row)
    max_value = max(min_value, max_value)

print(max_value)

## 예시 답안 ##

n, m = list(map(int, input().split()))

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)

    result = max(result, min_value)
        
print(result)