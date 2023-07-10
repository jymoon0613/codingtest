# 두 배열의 원소 교체

## 나의 답안 ##

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i] = B[i]
    
print(sum(A))

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
