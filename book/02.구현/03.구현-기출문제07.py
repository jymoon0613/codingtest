# 럭키 스트레이트

## 나의 답안 ##

N = input()

h = len(N) // 2

l = list(N[:h])
r = list(N[h:])

l_sum = sum([int(i) for i in l])
r_sum = sum([int(i) for i in r])

if l_sum == r_sum:
    print('LUCKY')

else:
    print('READY')

## 예시 답안 ##

n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')

else:
    print('READY')