# 2590: 색종이

array = [0] * 7
for i in range(1, 7):
    array[i] = int(input())

result = 0

if array[6]:
    result += array[6]

while array[5]:
    remain = 11
    array[5] -= 1
    array[1] = max(array[1]-remain, 0)
    result += 1

while array[4]:
    remain = 20 - (min(array[2], 5) * 4)
    array[4] -= 1
    array[2] = max(array[2]-5, 0)
    array[1] = max(array[1]-remain, 0)
    result += 1

while array[3]:
    remain = 36 - (min(array[3], 4) * 9)
    if array[3] >= 4:
        array[3] -= 4
        remain = 0
    elif array[3] == 3:
        remain -= (4 * min(array[2], 1))
        array[3] -= 3
        array[2] = max(array[2]-1, 0)
    elif array[3] == 2:
        remain -= (4 * min(array[2], 3))
        array[3] -= 2
        array[2] = max(array[2]-3, 0)
    else:
        remain -= (4 * min(array[2], 5))
        array[3] -= 1
        array[2] = max(array[2]-5, 0)

    array[1] = max(array[1]-remain, 0)
    result += 1

while array[2]:
    remain = 36 - (4 * min(array[2], 9))
    array[2] = max(array[2]-9, 0)
    array[1] = max(array[1]-remain, 0)
    result += 1

while array[1]:
    array[1] = max(array[1]-36, 0)
    result += 1

print(result)