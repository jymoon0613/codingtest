# 2138: 전구와 스위치

n = int(input())

array = list(map(int, input()))
target = list(map(int, input()))
    
def solution(array):

    arr = array[:]

    cnt = 0
    for i in range(1, n):
        if arr[i-1] != target[i-1]:
            cnt += 1
            arr[i-1] = 1 - arr[i-1]
            arr[i] = 1 - arr[i]
            if i < (n-1):
                arr[i+1] = 1 - arr[i+1]

    check = True
    for i in range(n):
        if arr[i] != target[i]:
            check = False
            break
    
    if check:
        return cnt
    else:
        return int(1e+9)
            
result = solution(array)

array[0] = 1 - array[0]
array[1] = 1 - array[1]

result = min(result, solution(array) + 1)

if result == int(1e+9):
    print(-1)
else:
    print(result)