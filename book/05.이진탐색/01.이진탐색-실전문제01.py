# 부품 찾기

## 나의 답안 ##

n = int(input())

data = list(map(int, input().split()))

m = int(input())

item = list(map(int, input().split()))

data.sort()

def binary_search(data, target, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2

    if data[mid] == target:
        return True
    
    elif data[mid] < target:
        return binary_search(data, target, mid+1, end)
    else:
        return binary_search(data, target, start, mid-1)

for i in range(m):

    if binary_search(data, item[i], 0, n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')

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