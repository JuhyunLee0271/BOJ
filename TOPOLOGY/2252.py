from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    x = q.popleft()
    result.append(x)
    for v in graph[x]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

print(*result)


