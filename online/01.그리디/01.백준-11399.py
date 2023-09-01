# 11399: ATM

n = int(input())

array = list(map(int, input().split()))

array.sort()

result = 0
sub_res = 0
for i in range(n):
    sub_res += array[i]
    result += sub_res

print(result)