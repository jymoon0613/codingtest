# 부품 찾기

## 나의 답안 ##

N = int(input())
items = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

items.sort()

def search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return search(array, target, start, mid-1)
    
    else:
        return search(array, target, mid+1, end)

res = []
for t in targets:
    if search(items, t, 0, N-1) == None:
        res.append('no')
    
    else:
        res.append('yes')
        
print(' '.join(res))

## 예시 답안 ##

def binary_search(array, target, start, end):
    
    while start <= end:
        
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
    
        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
            
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    
    else:
        print('no', end=' ')