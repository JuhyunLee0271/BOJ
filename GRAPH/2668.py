import sys
input = sys.stdin.readline

def DFS(node, target, visited):
    visited[node] = True
    for v in graph[node]:
        if not visited[v]:
            DFS(v, target, visited)
        elif visited[v] and v == target:
            result.append(v)

    pass

N = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
for i in range(N):
    graph[i+1].append(int(input()))

result = []
for i in range(1, N+1):
    DFS(i,i, [False]*(N+1))

print(len(result))
for e in result:
    print(e)
