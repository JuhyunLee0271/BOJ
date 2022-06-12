from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    rank = list(map(int, input().split()))

    for i in range(N):
        for j in range(i+1, N):
            graph[rank[i]].append(rank[j])
            indegree[rank[j]] += 1

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        
        if a not in graph[b]:
            a, b = b, a
        
        graph[b].remove(a)
        indegree[a] -= 1
        graph[a].append(b)
        indegree[b] += 1

    q = deque()
    answer = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    if not q:
        print("IMPOSSIBLE")
        continue
    
    while q:
        node = q.popleft()
        answer.append(node)
        for next in graph[node]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    print(*answer) if len(answer) == N else print("IMPOSSIBLE")
            
    