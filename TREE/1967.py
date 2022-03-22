import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(node, weight):
    for next, _weight in graph[node]:
        if dist[next] == -1:
            dist[next] = weight + _weight
            DFS(next, weight + _weight)

N = int(input())
graph = [[]* (N+1) for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dist = [-1] * (N+1)
dist[1] = 0
DFS(1, 0)

start = dist.index(max(dist))
dist = [-1] * (N+1)
dist[start] = 0
DFS(start, 0)
print(max(dist))