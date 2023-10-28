# 9082: 지뢰찾기

t = int(input())

for _ in range(t):
    
    n = int(input())

    array = list(map(int, input()))
    mine = list(input())
    result = 0
    for i in range(n):
        if i == 0:
            if array[i] != 0 and array[i+1] != 0:
                array[i] -= 1
                array[i+1] -= 1
                result += 1
        elif i == (n-1):
            if array[i-1] != 0 and array[i] != 0:
                array[i-1] -= 1
                array[i] -= 1
                result += 1
        else:
            if array[i-1] != 0 and array[i] != 0 and array[i+1] != 0:
                array[i-1] -= 1
                array[i] -= 1
                array[i+1] -= 1
                result += 1
    
    print(result)