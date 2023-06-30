# 볼링공 고르기

N, M = list(map(int, input().split()))
K = list(map(int, input().split()))

array = [0] * 11

for i in K:
    array[i] += 1

res = 0

for i in range(1, M+1):
    N -= array[i]
    res += array[i] * N
                
print(res)