# 1802: 종이접기

t = int(input())

def check(array):

    while len(array) >= 3:
        for i in range(0, len(array)-2, 2):
            if array[i] == array[i+2]:
                return False
    
        array_ = []
        for i in range(1, len(array), 2):
            array_.append(array[i])
        
        array = array_

    return True

for _ in range(t):
    pos = list(map(int, input()))
    if check(pos):
        print('YES')
    else:
        print('NO')