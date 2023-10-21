# 19539: 사과나무

n = int(input())

tree = list(map(int, input().split()))

def solution():

    if sum(tree) % 3:
        print('NO')
        return
    
    n2 = 0
    for i in range(n):
        n2 += tree[i] // 2

    if sum(tree) // 3 >= n2:
        print('NO')
        return
    
    else:
        print('YES')
        return
    
solution()