# 떡볶이 떡 만들기

## 나의 답안 ##

n, m = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

def get_sum(array, value):

    result = 0
    for x in array:
        if x > value:
            result += (x-value)

    return result

def binary_search(array, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        value = get_sum(array, mid)

        if value >= target:
            result = mid
            start = mid + 1

        else:
            end = mid - 1

    return result
            
result = binary_search(array, m, 0, array[-1])

print(result)

## 예시 답안 ##

n, m = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
            
    if total < m:
        
        end = mid - 1
        
    else:
        result = mid
        start = mid + 1
        
print(result)