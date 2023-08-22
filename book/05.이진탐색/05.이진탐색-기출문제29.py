# 공유기 설치

## 나의 답안 ##

n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

start = 1
end = array[n-1] - array[0]
result = None

while start <= end:

    mid = (start + end) // 2
    base = array[0]
    cnt = 1

    for i in range(1, n):
        if array[i] >= base + mid:
            cnt += 1
            base = array[i]
    
    if cnt < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

## 예시 답안 ##

n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while (start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1
    
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
            
        if count >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
            
print(result)