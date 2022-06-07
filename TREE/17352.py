import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return parents[x]
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b: return 
    elif a < b: parents[b] = a
    else: parents[a] = b

N = int(input())
parents = [i for i in range(N+1)]
for _ in range(N-2):
    a, b = map(int, input().split())
    union(a, b)

disjoint = set()
for node in parents[1:]:
    disjoint.add(find(node))

print(*list(disjoint))