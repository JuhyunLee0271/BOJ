from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c]) # [dst, cost]
    graph[b].append([a, c])
    
for _ in range(Q):
    k, v = map(int, input().split())
    usado = [1e9] * (N+1)
    answer = 0
    q = deque([v])
    
    while q:
        e = q.popleft()
        for x, dist in graph[e]:
            if x == v: continue
            if usado[x] == 1e9:
                usado[x] = min(dist, usado[e])
                q.append(x)
                if usado[x] >= k:
                    answer += 1
    print(answer)
        
    
        