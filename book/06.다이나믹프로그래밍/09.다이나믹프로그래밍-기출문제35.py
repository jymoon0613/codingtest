# 못생긴 수

## 나의 답안 ##

n = int(input())

d = [0] * n

d[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    d[i] = min(next2, next3, next5)

    if d[i] == next2:
        i2 += 1
        next2 = d[i2] * 2
    if d[i] == next3:
        i3 += 1
        next3 = d[i3] * 3
    if d[i] == next5:
        i5 += 1
        next5 = d[i5] * 5

print(d[n-1])

## 예시 답안 ##

n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0

next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    
    ugly[l] = min(next2, next3, next5)
    
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
        
print(ugly[n-1])