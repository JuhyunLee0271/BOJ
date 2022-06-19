import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(node):
    global count
    visited[node] = count
    
    for x in graph[node]:
        if visited[x] == 0:
            count += 1
            DFS(x)
    return

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort(reverse=True)

DFS(R)

for e in visited[1:]:
    print(e)