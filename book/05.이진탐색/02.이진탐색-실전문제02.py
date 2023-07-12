# 떡볶이 떡 만들기

## 나의 답안 ##

def check(array, target):
    res = 0
    for a in array:
        if a < target:
            continue
        else:
            res += a - target
            
    return res

def search(array, target, start, end):
    
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if check(array, mid) == target:
        return mid
    
    elif check(array, mid) < target:
        return search(array, target, start, mid-1)
        
    else:
        return search(array, target, mid+1, end)
    
n, m = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

search(array, m, 0, array[-1])

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