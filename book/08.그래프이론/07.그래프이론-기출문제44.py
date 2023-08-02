# 행성 터널

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
        
n = int(input())

nodes = []

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i
    
for _ in range(n):
    x, y, z = map(int, input().split())
    nodes.append((x, y, z))
    
res = 0
groups = []
for i in range(1, n+1):
    node = nodes[i-1]
    parent[i] = -1
    if len(groups) != 0:
        min_dist = int(1e+9)
        for g in groups:
            nx, ny, nz = g
            x, y, z = node
            dist = min(abs(nx-x), abs(ny-y), abs(nz-z))
            min_dist = min(dist, min_dist)
        res += min_dist
    groups.append(node)
    
print(res)

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
        
n = int(input())

parent = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i
    
x = []
y = []
z = []
    
for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
    
x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))
    
edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
    
print(result)