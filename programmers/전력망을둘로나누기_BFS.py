from itertools import combinations
from collections import deque
import sys

def BFS(x, visited, graph):
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        x = q.popleft()
        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    
    return visited[1:].count(True)

def solution(n, wires):
    answer = sys.maxsize
    for pairs in combinations(wires, n-2):
        graph = [[] for _ in range(n+1)]
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)
        result = BFS(1, [False] * (n+1), graph)
        answer = min(answer, abs(2*result -n))
    return answer