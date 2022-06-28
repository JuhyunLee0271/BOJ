import sys
input = sys.stdin.readline

def bipartite_matching(node):
    if visited[node]:
        return False
    visited[node] = True
    
    for match in graph[node]:
        if selected[match] == -1 or bipartite_matching(selected[match]):
            selected[match] = node
            return True
    return False

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
selected = [-1] * (M+1)

for i in range(1, N+1):
    graph[i].extend(list(map(int, input().split()[1:])))

for i in range(1, N+1):
    visited = [False] * (N+1)
    bipartite_matching(i)

print(len([match for match in selected[1:] if match != -1]))