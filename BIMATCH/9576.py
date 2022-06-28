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

for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(M+1)]
    for i in range(M):
        a, b = map(int, input().split())
        for num in range(a, b+1):
            graph[i+1].append(num)

    selected = [-1] * (N+1)

    for i in range(1, M+1):
        visited = [False] * (M+1)
        bipartite_matching(i)

    print(len([node for node in selected[1:] if node != -1]))