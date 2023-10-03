# 1239: 차트

import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

result = 0
if max(array) > 50:
    print(0)
else:
    for candidate in permutations(array):
        accum_list = []
        accum_value = 0
        mid_ans = 0
        for num in candidate:
            accum_value += num
            accum_list.append(accum_value)
        for i in range(len(accum_list)-1):
            for j in range(i+1, len(accum_list)):
                if accum_list[i] + 50 == accum_list[j]:
                    mid_ans += 1
        result = max(result, mid_ans)
    print(result)