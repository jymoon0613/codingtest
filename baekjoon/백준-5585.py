# 5585: 거스름돈

n = int(input())

target = 1000 - n

cnt = 0
while target != 0:

    if target >= 500:
        cnt += target // 500
        target %= 500

    if target >= 100:
        cnt += target // 100
        target %= 100

    if target >= 50:
        cnt += target // 50
        target %= 50

    if target >= 10:
        cnt += target // 10
        target %= 10

    if target >= 5:
        cnt += target // 5
        target %= 5
    
    if target >= 1:
        cnt += 1
        target -= 1

print(cnt)