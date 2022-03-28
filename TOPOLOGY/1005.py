from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    dist = [0] * (N+1)
    cost = [0] + list(map(int, input().split()))
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    W = int(input())

    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dist[i] = cost[i]

    while q:
        x = q.popleft()
        for v in graph[x]:
            indegree[v] -= 1
            dist[v] = max(dist[v], dist[x] + cost[v])
            if indegree[v] == 0:
                q.append(v)

    print(dist[W])