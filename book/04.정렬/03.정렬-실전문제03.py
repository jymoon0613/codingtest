# 두 배열의 원소 교체

## 나의 답안 ##

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

cnt = 0
for i in range(n):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
        cnt += 1
    if cnt >= k:
        break

print(sum(a))

## 예시 답안 ##

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
    
print(sum(a))
