import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b: return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    command, a, b = map(int, input().split())    
    if command == 0:
        union(a,b)
    elif command == 1:
        if find(a) == find(b): print("YES")
        else: print("NO")
