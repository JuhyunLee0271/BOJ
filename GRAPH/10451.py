from collections import deque
import sys
input = sys.stdin.readline

def BFS(x):
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        x = q.popleft()
        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

T = int(input())
for _ in range(T):
    N = int(input())
    visited = [False] * (N+1)
    graph = [[]*(N+1) for _ in range(N+1)]
    numbers = list(map(int, input().split()))

    for idx, num in enumerate(numbers):
        graph[idx+1].append(num)
    
    result = 0
    for i in range(1, N+1):
        if not visited[i]:
            BFS(i)
            result += 1
    print(result)
