from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
dist = [sys.maxsize] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append((X))
visited[X] = True
dist[X] = 0

while q:
    x = q.popleft()
    for v in graph[x]:
        if not visited[v]:
            visited[v] = True
            dist[v] = dist[x] + 1
            q.append(v)

result = [i for i in range(len(dist)) if dist[i] == K]

if result:
    for e in result:
        print(e)
else:
    print(-1)
    
