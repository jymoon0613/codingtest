# 자물쇠와 열쇠

## 나의 답안 ##

import json
import copy

key = input()
lock = input()

key = json.loads(key)
lock = json.loads(lock)

def turn_key(key):
    output = [[0] * len(key) for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(key)):
            output[i][j] = key[j][len(key)-1-i]

    return output

def check(array_copy, lock, offset):
    res = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            res += array_copy[i+offset][j+offset]

    if res == (len(lock) ** 2):
        return True
    
    else:
        return False

def solution(key, lock):

    offset = len(key) - 1

    array = [[0] * (len(lock) + 2 * offset) for _ in range(len(lock) + 2 * offset)]

    for i in range(len(lock)):
        for j in range(len(lock)):
            array[i+offset][j+offset] = lock[i][j]
    
    for _ in range(4):
        
        key = turn_key(key)

        for i in range(len(lock) + offset):
            for j in range(len(lock) + offset):
                array_copy = copy.deepcopy(array)
                for x in range(len(key)):
                    for y in range(len(key)):
                        array_copy[x+i][y+j] += key[x][y]
                if check(array_copy, lock, offset):
                    print('true')
                    return
                        
    print('false')
    return

solution(key, lock)

## 예시 답안 ##

import json

key = input()
lock = input()

key = json.loads(key)
lock = json.loads(lock)

def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]

    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n*3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(m):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(n):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock) == True:
                    return True
                
                for i in range(n):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
                        
print(solution(key, lock))