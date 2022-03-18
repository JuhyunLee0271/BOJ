from collections import deque

def BFS(arr, visited, start):
    q = deque()
    q.append(start)
    visited[start] = True
    cnt = 0 

    while q:
        v = q.popleft()
        for e in arr[v]:
            if not visited[e]:
                visited[e] = True
                cnt += 1
                q.append(e)

    return cnt

N = int(input())
arr = []
for _ in range(N+1):
    arr.append([])
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False] * (N+1)
print(BFS(arr, visited, 1))

