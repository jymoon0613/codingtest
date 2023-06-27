# 모험가 길드

N = int(input())
F = list(map(int, input().split()))

F.sort()

res = 0
cnt = 0

for i in F:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0
        
print(cnt)