# 14888: 연산자 끼워넣기

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))

max_value = -int(1e+9)
min_value = int(1e+9)
def dfs(total, index):

    global max_value, min_value, a, o

    if index >= n:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return

    if o[0] > 0:

        o[0] -= 1
        dfs(total + a[index], index+1)
        o[0] += 1

    if o[1] > 0:

        o[1] -= 1
        dfs(total - a[index], index+1)
        o[1] += 1

    if o[2] > 0:

        o[2] -= 1
        dfs(total * a[index], index+1)
        o[2] += 1

    if o[3] > 0:

        o[3] -= 1
        dfs(int(total / a[index]), index+1)
        o[3] += 1

dfs(a[0], 1)

print(max_value)
print(min_value)