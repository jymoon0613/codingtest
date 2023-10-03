# 1025: 제곱수 찾기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

def binary_search(num, start, end):

    while start <= end:

        mid = (start + end) // 2

        if mid**2 == num:
            return mid

        if mid**2 > num:
            end = mid - 1

        else:
            start = mid + 1

    return None

max_value = 0
max_length = max(n,m)


