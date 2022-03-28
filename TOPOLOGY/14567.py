from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
dist = [INF] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        dist[i] = 1

while q:
    x = q.popleft()
    for v in graph[x]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
            dist[v] = dist[x] + 1

print(*dist[1:])