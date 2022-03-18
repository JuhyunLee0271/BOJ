from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [0] * (N+1)
q = deque()
q.append(1)

while q:
    x = q.popleft()
    for v in graph[x]:
        if not parents[v]:
            parents[v] = x
            q.append(v)

for e in parents[2:]:
    print(e)

    
