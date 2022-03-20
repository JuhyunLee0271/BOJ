from collections import deque
import sys
input = sys.stdin.readline

def BFS(arr, start):
    q = deque()
    q.append((start, 0))
    visited = [False] * (N+1)
    visited[start] = True
    cost = [0] * (N+1)

    while q:
        x, w = q.popleft()
        for e in arr[x]:
            if not visited[e]:
                visited[e] = True
                cost[e] = w + 1
                q.append((e, w+1))
    
    return sum(cost)

N, M = map(int, input().split())
arr = [[] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

result = []
for i in range(1, N+1):
    result.append(BFS(arr, i))
print(result.index(min(result))+1)
