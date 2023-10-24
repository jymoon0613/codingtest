# 2891: 카약과 강풍

n, s, r = map(int, input().split())

num_crash = list(map(int, input().split()))
num_remain = list(map(int, input().split()))

num_crash.sort()
num_remain.sort()

result = 0
for num in num_crash:
    if num in num_remain:
        num_remain.remove(num)
    elif num-1 in num_remain:
        if num-1 not in num_crash:
            num_remain.remove(num-1)
        else:
            result += 1
    elif num+1 in num_remain:
        if num+1 not in num_crash:
            num_remain.remove(num+1)
        else:
            result += 1
    else:
        result += 1

print(result)