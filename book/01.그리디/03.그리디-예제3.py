# 1이 될 때까지

N, K = list(map(int, input().split()))

cnt = 0

while (N % K != 0):
    N -= 1
    cnt += 1
    
while N != 1:
    N /= K
    cnt += 1

print(cnt)