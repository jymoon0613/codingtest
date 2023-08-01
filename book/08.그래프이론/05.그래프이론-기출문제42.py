# 탑승구

## 나의 답안 ##

g = int(input())
p = int(input())

graph = [0] * (p+1)

for i in range(1, p+1):
    graph[i] = int(input())
    
cnt = 1
check = True
for i in range(2, p+1):
    cnt += 1    
    for j in range(1, i+1):
        graph[j] -= graph[i]
    for a in graph[1:]:
        if a <= 0:
            check = False
            break
    if check == False:
        break
print(cnt)

## 예시 답안 ##

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = int(input())
p = int(input())

parent = [0] * (g+1)

for i in range(1, g+1):
    parent[i] = i
    
result = 0
for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union_parent(parent, data, data-1)
    result += 1
    
print(result)