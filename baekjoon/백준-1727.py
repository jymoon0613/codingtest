# 1727: 커플 만들기

n, m = map(int, input().split())
man = list(map(int, input().split()))
woman = list(map(int, input().split()))

man.sort()
woman.sort()

d = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] = d[i-1][j-1] + abs(man[i-1]-woman[j-1])
        if i > j:
            d[i][j] = min(d[i][j], d[i-1][j])
        elif i < j:
            d[i][j] = min(d[i][j], d[i][j-1])

print(d[n][m])