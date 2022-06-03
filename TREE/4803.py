from collections import deque
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

idx = 0
while True:
    idx += 1
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    parent = [i for i in range(N+1)]
    cycle = set()
    for _ in range(M):
        a, b = map(int, input().split())
        if find(a) == find(b):
            cycle.add(parent[a])
            cycle.add(parent[b])
        if parent[a] in cycle or parent[b] in cycle:
            cycle.add(parent[a])
            cycle.add(parent[b])
        union(a, b)

    for i in range(N+1):
        find(i)

    parent = set(parent)
    answer = sum([1 if i not in cycle else 0 for i in parent]) - 1

    if answer == 0: print(f"Case {idx}: No trees.")
    elif answer == 1: print(f"Case {idx}: There is one tree.")
    else: print(f"Case {idx}: A forest of {answer} trees.")

