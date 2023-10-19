# 13975: 파일 합치기 3

import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    size = list(map(int, input().split()))
    q = []
    for i in range(k):
        heapq.heappush(q, size[i])

    result = 0
    while len(q) > 1:

        s1 = heapq.heappop(q)
        s2 = heapq.heappop(q)

        result += (s1+s2)

        heapq.heappush(q, s1+s2)

    print(result)