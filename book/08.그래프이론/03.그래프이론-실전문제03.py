# 커리큘럼

## 나의 답안 ##

from collections import deque
import copy

n = int(input())
indegree = [0] * (n+1)
time = [0] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] += data[0]
    data = data[:-1]
    for j in range(1, len(data)):
        graph[data[j]].append(i)
        indegree[i] += 1
        
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
    for i in range(1, n+1):
        print(result[i])
    
topology_sort()

## 예시 답안 ##

from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] += data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
        
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
    for i in range(1, v+1):
        print(result[i])
    
topology_sort()