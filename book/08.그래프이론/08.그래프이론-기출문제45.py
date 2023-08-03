# 최종 순위

## 나의 답안 ##

from collections import deque

for tc in range(int(input())):
    
    n = int(input())

    indegree = [0] * (n+1)

    graph = [[0] * (n+1) for _ in range(n+1)]

    rank = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            graph[rank[i]][rank[j]] = 1
            indegree[rank[j]] += 1

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b] == 1:
            graph[a][b] = 0
            graph[b][a] = 1
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = 1
            graph[b][a] = 0
            indegree[a] -= 1
            indegree[b] += 1

    def topology_sort():
        result = []
        q = deque()
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)

        cycle = False
        redun = False
        while q:
            now = q.popleft()
            result.append(now)
            for j in range(1, n+1):
                if graph[now][j] == 1:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        q.append(j)
            if len(q) >= 2:
                redun = True
                print('?')
                break
        if len(result) != n:
            cycle = True
            print('IMPOSSIBLE')

        if redun == False and cycle == False:
            for r in result:
                print(r, end=' ')

    topology_sort()

## 예시 답안 ##

from collections import deque

for tc in range(int(input())):
    
    n = int(input())

    indegree = [0] * (n+1)

    graph = [[False] * (n+1) for i in range(n+1)]

    data = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b] == 1:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False
    
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
            
        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print('IMPOSSIBLE')
        
    elif not certain:
        print('?')

    else:
        for i in result:
            print(i, end=' ')