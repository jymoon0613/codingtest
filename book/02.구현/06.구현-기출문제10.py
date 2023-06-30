# 자물쇠와 열쇠

## 나의 답안 ##

import json
import copy

key = input()
lock = input()

key = json.loads(key)
lock = json.loads(lock)

def rotate(key, r):
    
    if r == 'none':
        
        key_s = key
        
    elif r == '90':
        
        key_s = rotation(key)
        
    elif r == '180':
        
        key_s = rotation(key)
        key_s = rotation(key_s)
        
    else:
        key_s = rotation(key)
        key_s = rotation(key_s)
        key_s = rotation(key_s)
        
    return key_s
        

def rotation(key):
    
    r = len(key)
    c = len(key[0])
    
    key_t = [[0] * c for _ in range(r)]
    
    # transpose
    for i in range(r):
        for j in range(c):
            key_t[i][j] = key[j][i]
    
    key_r = [[0] * c for _ in range(r)]
    
    # vertical flip
    for i in range(r):
        for j in range(c):
            key_r[i][j] = key_t[i][c-1-j]
    
    
    return key_r

def shift(key, d):
    
    r = len(key)
    c = len(key[0])
    
    key_s = [[0] * c for _ in range(r)]
    
    if d == 'none':
        for i in range(r):
            for j in range(c):
                key_s[i][j] = key[i][j]
    
    elif d == 'top':
        for i in range(r):
            for j in range(c):
                if (i + 1) < r:
                    key_s[i][j] = key[i+1][j]
                else:
                    key_s[i][j] = 0
        
    elif d == 'down':
        for i in range(r):
            for j in range(c):
                if (i - 1) >= 0:
                    key_s[i][j] = key[i-1][j]
                else:
                    key_s[i][j] = 0
    
    elif d == 'left':
        for i in range(r):
            for j in range(c):
                if (j + 1) < c:
                    key_s[i][j] = key[i][j+1]
                else:
                    key_s[i][j] = 0
                    
    else:
        for i in range(r):
            for j in range(c):
                if (j - 1) >= 0:
                    key_s[i][j] = key[i][j-1]
                else:
                    key_s[i][j] = 0
    
    return key_s

def check(key, lock):
    
    r = len(lock)
    c = len(lock[0])
    
    checker = [[0] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            
            if (key[i][j] == 1) and (checker[i][j] == 1):
                return 0
            
            elif (key[i][j] == 1) and (checker[i][j] == 0):
                checker[i][j] = 1
            
            else:
                checker[i][j] = lock[i][j]

    if sum([sum(row) for row in checker]) == r_l * c_l:
        
        return 1
    
    else:
        
        return 0
    
def solution(key, lock):
    
    r_l = len(lock)
    c_l = len(lock[0])

    r_k = len(key)
    c_k = len(key[0])

    pad = r_l - r_k

    if pad != 0:

        key = [row + [0] * pad for row in key]
    
    rotations = ['none', '90', '180', '270']
    shifts = ['none', 'top', 'down', 'left', 'right']

    range_shift = r_k - 1

    for rot in rotations:

        key_copy = copy.deepcopy(key)

        key_copy = rotate(key_copy, rot)

        for shi1 in shifts:
            for _ in range(range_shift):
                key_copy = shift(key_copy, shi1)
                for shi2 in shifts:
                    for _ in range(range_shift):
                        key_copy = shift(key_copy, shi2)

                        res = check(key_copy, lock)

                        if res == 1:
                            return 'true'
                        
    return 'false'

print(solution(key, lock))

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