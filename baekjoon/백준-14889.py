# 14889: 스타트와 링크

import sys

input = sys.stdin.readline

N = int(input())
array = []
result = 1e9
visited = [False] * (N + 1)
for _ in range(N):
    array.append(list(map(int, input().split())))


def solve(depth, idx):
    global result
    if depth == (N // 2):
        start, link = 0, 0 
        for i in range(N): 
            for j in range(i + 1, N):  
                if visited[i] and visited[j]:
                    start += (array[i][j] + array[j][i])
                elif not visited[i] and not visited[j]:
                    link += (array[i][j] + array[j][i])
        
        result = min(result, abs(start - link))
    for i in range(idx, N): 
        if not visited[i]:
            visited[i] = True
            solve(depth + 1, i + 1)
            visited[i] = False


solve(0, 0)
print(result)