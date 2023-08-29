# 어두운 길

## 나의 답안 ##

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

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

edges = []
total = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))
    total += z

edges.sort()

for edge in edges:

    z, x, y = edge

    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        total -= z

print(total)

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

n, m = map(int, input().split())

parent = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i
    
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))
    
edges.sort()
total = 0

for edge in edges:
    cost, a, b = edge
    total += cost
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(total - result)