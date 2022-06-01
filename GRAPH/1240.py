from collections import deque
import sys
input = sys.stdin.readline

def BFS(start, end):
    visited = [False]*(N+1)
    visited[start] = True
    q = deque()
    q.append([start, 0])
    
    while q:
        x, dist = q.popleft()
        if x == end:
            return dist
        for node, _dist in graph[x]:
            if not visited[node]:
                visited[node] = True
                q.append([node, dist + _dist])
    
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

for _ in range(M):
    n1, n2 = map(int, input().split())
    print(BFS(n1, n2))

    