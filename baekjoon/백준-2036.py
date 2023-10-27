# 2036: 수열의 점수

n = int(input())

plus = []
minu = []
cnt_0 = 0
for i in range(n):
    a = int(input())
    if a == 0:
        cnt_0 += 1
    elif a < 0 :
        minu.append(a)
    else:
        plus.append(a)

minu.sort()
plus.sort(reverse=True)

result = 0
for i in range(0, len(minu)-1, 2):
    result += (minu[i] * minu[i+1])
if len(minu) % 2 != 0:
    if cnt_0 == 0:
        result += minu[-1]

for i in range(0, len(plus)-1, 2):
    if plus[i] != 1 and plus[i+1] != 1:
        result += (plus[i] * plus[i+1])
    else:
        result += (plus[i] + plus[i+1])
if len(plus) % 2 != 0:
    result += plus[-1]

print(result)