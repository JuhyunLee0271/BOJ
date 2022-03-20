from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

def BFS(x):
    q = deque()
    q.append(x)
    visited = [False] * (N+1)
    visited[x] = True
    count = 0

    while q:
        x = q.popleft()
        for e in graph[x]:
            if not visited[e]:
                visited[e] = True
                count += 1
                q.append(e)
    return count

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = INF
    for i in range(1, N+1):
        result = min(result, BFS(i))
    print(result)
    

