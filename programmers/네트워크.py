from collections import deque

def BFS(x, visited, graph):
    q = deque([x])
    visited[x] = True
    
    while q:
        x = q.popleft()
        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    
    for i in range(len(computers)):
        for j in range(i, len(computers[i])):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            BFS(i, visited, graph)
            answer += 1   
    
    return answer