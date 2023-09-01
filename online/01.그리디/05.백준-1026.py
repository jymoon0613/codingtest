# 1026: 보물

n = int(input())

a = list(map(int, input().split()))
b = list(map(int ,input().split()))

result = 0
for i in range(n):
    min_a = min(a)
    max_b = max(b)

    result += (min_a * max_b)

    a.remove(min_a)
    b.remove(max_b)

print(result)