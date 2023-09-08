# 정렬된 배열에서 특정 수의 개수 구하기

## 나의 답안 1 ##

n, x = map(int, input().split())

array = list(map(int, input().split()))

def binary_search_left(array, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if array[mid] == target and (mid == 0 or array[mid-1] != target):
            
            return mid
        
        elif array[mid] >= target:

            return binary_search_left(array, target, start, mid-1)
        
        else:

            return binary_search_left(array, target, mid+1, end)
        
def binary_search_right(array, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if array[mid] == target and (mid == (n-1) or array[mid+1] != target):
            
            return mid
        
        elif array[mid] > target:

            return binary_search_right(array, target, start, mid-1)
        
        else:

            return binary_search_right(array, target, mid+1, end)
        
a = binary_search_left(array, x, 0, n-1)
b = binary_search_right(array, x, 0, n-1)

if a == None or b == None:
    print(-1)
else:
    print(b-a+1)

## 나의 답안 2 ##

import bisect

n, x = map(int, input().split())

array = list(map(int, input().split()))

a = bisect.bisect_left(array, x)
b = bisect.bisect_right(array, x)

if a == n and b == n:
    print(-1)
else:
    print(b-a)

## 예시 답안 ##

def count_by_value(array, x):
    n = len(array)
    
    a = first(array, x, 0, n-1)
    
    if a == None:
        return 0
    
    b = last(array, x, 0, n-1)
    
    return b - a + 1

def first(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    
    else:
        return first(array, target, mid+1, end)
    
def last(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    
    else:
        return last(array, target, mid+1, end)
    
n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)