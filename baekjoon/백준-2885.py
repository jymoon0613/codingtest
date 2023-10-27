# 2885: 초콜릿 식사

k = int(input())
total = 1
cnt = 0
while total < k:

    total += total

    cnt += 1

cnt = 0
base = total
while True:

    if k % base == 0:
        break

    base -= (base // 2)

    cnt += 1

print(total, cnt)