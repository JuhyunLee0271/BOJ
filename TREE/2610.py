from collections import deque
import sys
input = sys.stdin.readline

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    a, b = find(a), find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

def BFS(x):
    visited = [False] * (N+1)
    visited[x] = True
    q = deque()
    q.append([x, 0]) # [node, distance]
    distances = [0]
    
    while q:
        x, dist = q.popleft()
        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                distances.append(dist + 1)
                q.append([v, dist + 1])
    
    return max(distances)
    
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)
    graph[a].append(b)
    graph[b].append(a)

disjoint = []
p = set()
for i in range(1, N+1):
    p.add(find(i))

for _p in list(p):
    temp = []
    for i in range(1, N+1):
        if find(i) == _p:
            temp.append(i)
    disjoint.append(temp)

answer = []
for tree in disjoint:
    max_vals = []
    for _node in tree:
        max_vals.append(BFS(_node))
    answer.append(tree[max_vals.index(min(max_vals))])

print(len(answer))
for node in sorted(answer):
    print(node)